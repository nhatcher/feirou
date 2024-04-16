import json
import logging
from datetime import timedelta

# from typing import TYPE_CHECKING
from uuid import uuid4

import requests
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpRequest, JsonResponse
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_POST

# We want to be able to mock the email sending on the tests, doing:
# from .email import send_confirmation_email
# would make that impossible
from users import email

from .models import PendingUser, RecoverPassword, SupportedLocales

logger = logging.getLogger(__name__)


# pyright issues
# A user request is an authenticated user
class UserRequest(HttpRequest):
    user: User


@require_POST
@csrf_exempt
def update_password(request: HttpRequest) -> JsonResponse:
    """Updates password of user from an email_token"""
    logger.info("User updates password")

    data = json.loads(request.body)
    logger.info(request.body)

    password: str = data["password"]
    email_token: str = data["email-token"]

    recover_password = RecoverPassword.objects.get(email_token=email_token)

    try:
        validate_password(password)
    except ValidationError as e:
        return JsonResponse(
            {"details": e.messages[0], "message": _("invalid-password")}, status=400
        )

    user = recover_password.user
    user.set_password(password)
    user.save()
    logger.info(f"Password for {user.username} updated")

    recover_password.delete()

    return JsonResponse(
        {
            "details": "Password successfully updated.",
            "message": _("password-updated-successfully"),
        }
    )


@require_POST
@csrf_exempt
def recover_password(request: HttpRequest) -> JsonResponse:
    """Send a link via email to a user so they can update their password"""
    data = json.loads(request.body)
    email_address: str = data["email"]
    logger.info(f"Retrieving user with email: {email_address}")

    try:
        user = User.objects.get(email=email_address)
    except Exception:
        return JsonResponse(
            {"details": "User not found", "message": _("user-not-found")}, status=400
        )
    username: str = user.username

    email_token: str = str(uuid4())

    requested_date = timezone.now()
    # links expire 2 hours after creation
    expiration_date = requested_date + timedelta(hours=2)

    recover_password = RecoverPassword.objects.create(
        user=user,
        email_token=email_token,
        requested_date=requested_date,
        expiration_date=expiration_date,
    )
    recover_password.save()

    locale = user.userprofile.locale.code  # type: ignore

    email.send_update_password_email(email_address, username, email_token, locale)

    return JsonResponse({"details": "Email sent."})


def activate_account(request: HttpRequest, email_token: str) -> JsonResponse:
    """Activates a user account. This is normally done via visiting link"""
    try:
        pending_user = PendingUser.objects.get(email_token=email_token)
    except Exception:
        logger.warning("Could not find a user to activate")
        return JsonResponse(
            {
                "details": "Could not find a user to activate",
                "message": _("no-user-to-activate"),
            },
            status=400,
        )

    user = pending_user.user_profile.user
    user.is_active = True
    user.save()

    pending_user.delete()

    logger.info("User activated and pending user deleted!")
    if settings.DISCORD_URL:
        requests.post(settings.DISCORD_URL, {"content": "New user activated!"})
    return JsonResponse({"details": "Account successfully activated."})


@require_POST
def create_account(request: HttpRequest) -> JsonResponse:
    """Creates an inactive account for a user"""
    logger.info("Creating account for user")

    data = json.loads(request.body)
    username: str = data["username"]
    email_address: str = data["email"]
    password: str = data["password"]

    assert request.headers["Accept-Language"] == data["locale"]

    # validate data server side
    try:
        validate_email(email_address)
        validate_password(password)
    except ValidationError as e:
        logger.warning(f"We found a problem validating your password: {str(e)}")
        return JsonResponse(
            {"details": str(e), "message": _("invalid-email-password")}, status=400
        )

    # create user and set as inactive
    try:
        user = User.objects.create_user(username, email_address, password)
    except Exception as e:
        logger.warning(f"We found a problem while creating account: {str(e)}")
        return JsonResponse(
            {"details": repr(e), "message": _("cant-create-user")}, status=400
        )
    user.is_active = False

    locale = SupportedLocales.objects.get(code=data["locale"])

    user.userprofile.locale = locale  # type: ignore

    user.save()

    logger.info("Inactive user created")

    email_token: str = str(uuid4())

    # create pending user
    pending_user: PendingUser = PendingUser.objects.create(
        user_profile=user.userprofile, email_token=email_token  # type: ignore
    )
    pending_user.save()

    logger.info("Pending user created")

    # send confirmation email
    locale = user.userprofile.locale.code  # type: ignore
    email.send_confirmation_email(email_address, username, email_token, locale)

    logger.info("Confirmation email sent")
    return JsonResponse(
        {
            "details": "Successfully user created.",
            "message": _("user-created-successfully"),
        }
    )


@require_POST
def login_view(request: HttpRequest) -> JsonResponse:
    """Logs user in if username and password are correct"""
    logger.info("Login attempt")

    data = json.loads(request.body)
    username: str = data["username"]
    password: str = data["password"]

    user = authenticate(username=username, password=password)

    if user is None:
        logger.warning("Invalid credentials")
        print(_("invalid-email-password"))
        return JsonResponse(
            {"details": "Invalid credentials.", "message": _("invalid-credentials")},
            status=400,
        )

    login(request, user)
    logger.info("Successfully logged in")

    return JsonResponse(
        {"details": "Successfully logged in.", "message": _("logged-in-successfully")}
    )


@require_POST
def logout_view(request: HttpRequest) -> JsonResponse:
    logger.info("Login out")
    if not request.user.is_authenticated:
        return JsonResponse({"details": "You are not logged in."}, status=400)

    logout(request)

    logger.info("Logged out")
    return JsonResponse({"details": "Successfully logged out."})


@ensure_csrf_cookie
def session_view(request: UserRequest) -> JsonResponse:
    if not request.user.is_authenticated:
        return JsonResponse({"authenticated": False})

    return JsonResponse(
        {
            "authenticated": True,
            "username": request.user.username,
            "first-name": request.user.first_name,
            "last-name": request.user.last_name,
        }
    )


# TODO: remove this because it is the same as 'session_view'
@require_POST
def whoami(request: UserRequest) -> JsonResponse:
    if not request.user.is_authenticated:
        return JsonResponse({"authenticated": False})

    user = request.user
    return JsonResponse(
        {
            "username": user.username,
            "first-name": user.first_name,
            "last-name": user.last_name,
            "authenticated": True,
        }
    )


def trigger_error(request) -> JsonResponse:
    """Raises an exception. Useful for testing"""
    division_by_zero = 1 / 0
    return JsonResponse({"result": division_by_zero})  # pragma: no cover


def say_hello(request) -> JsonResponse:
    """Responds 'Hello!' or 'Olá! depending on language. Useful for testing"""
    return JsonResponse({"message": _("say_hello")})
