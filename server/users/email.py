from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_email(recipient: str, username: str, email_token: str):
    """Sends confirmation email"""
    app_url = settings.APP_URL

    message = """
    Hello %(username)s, we need to confirm your email.

    Please click in the link bellow:

    %(app_url)sapi/activate-account/%(email_token)s

    If you have not asked for an account in this platform you can ignore this message.

    Greetings,
    %(app_url)s
    """ % {
        "username": username,
        "app_url": app_url,
        "email_token": email_token,
    }

    subject = "Confirm your email"

    send_mail(subject, message, None, [recipient])


def send_update_password_email(recipient: str, username: str, email_token):
    """Sends update password link"""
    app_url = settings.APP_URL

    message = """
    Hi %(username)s, you have requested to reset your password.

    Please click in the link bellow:

    %(app_url)supdate_password.html#id=%(email_token)s

    If you have not asked for an account in this platform you can ignore this message.

    Greetings,
    %(app_url)s
    """ % {
        "username": username,
        "app_url": app_url,
        "email_token": email_token,
    }

    subject = "Update password"

    send_mail(subject, message, None, [recipient])
