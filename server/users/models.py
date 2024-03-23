from __future__ import annotations

from django.contrib.auth.models import User
from django.db import models


class SupportedLocales(models.Model):
    """List of supported locales in the platform"""

    code = models.CharField(max_length=5)
    name = models.TextField(max_length=120, default="")


class UserProfile(models.Model):
    """Extends the internal django User Model with extra data"""

    user = models.OneToOneField(
        User,
        related_name="userprofile",
        related_query_name="userprofile",
        on_delete=models.CASCADE,
    )
    locale = models.ForeignKey(SupportedLocales, on_delete=models.CASCADE, default=1)


class PendingUser(models.Model):
    """
    A pending-user has not yet confirmed the email link.

    We use a real User with `is_active = False`. This ensures things like
    unique username, valid password, etc...

    Once the link is confirmed `is_active` will be set to True and the pending-user deleted
    """

    # In principle there can be many "pending-users" pointing to the same user
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=120, default="")


class RecoverPassword(models.Model):
    """This is a list of folks that have requested a recover password link"""

    email_token = models.CharField(max_length=120, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
