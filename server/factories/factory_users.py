"""
This module defines factories for models related to users, including SupportedLocales, 
UserProfile, PendingUser, and RecoverPassword, using Factory Boy for generating test data.
"""

import random
from datetime import timedelta

import factory
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import PendingUser, RecoverPassword, SupportedLocales, UserProfile


class SupportedLocalesFactory(factory.django.DjangoModelFactory):
    """Creates instances of SupportedLocales with predefined locale codes ('en-US', 'pt-BR')."""

    class Meta:
        model = SupportedLocales
        django_get_or_create = (
            "code",
        )  # This ensures existing locales are reused instead of created anew

    # Example locale codes. Adjust as necessary based on your actual locale codes.
    code = factory.Iterator(["en-US", "pt-BR"])
    name = factory.LazyAttribute(lambda obj: f"Locale for {obj.code}")


class UserFactory(factory.django.DjangoModelFactory):
    """Generates fake User instances with randomized usernames, emails, first names,
    and activation status."""

    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = factory.Faker("first_name")
    is_active = factory.Iterator([True, False])


class UserProfileFactory(factory.django.DjangoModelFactory):
    """Produces UserProfile instances linked to User instances. Each profile is
    associated with a locale, created using the SupportedLocalesFactory"""

    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    locale = factory.SubFactory(SupportedLocalesFactory)


class PendingUserFactory(factory.django.DjangoModelFactory):
    """Creates PendingUser instances representing users who have registered but
    not yet confirmed their email. Each pending user is linked to a UserProfile
    and is assigned a fake UUID as an email token"""

    class Meta:
        model = PendingUser

    # Assume que você tem uma UserProfileFactory para gerar perfis de usuário
    user_profile = factory.SubFactory(UserProfileFactory)

    # Gera um token de email fictício usando um UUID
    email_token = factory.Faker("uuid4")


def random_datetime_last_30_days():
    now = timezone.now()
    start = now - timedelta(days=30)
    random_date = start + random.random() * (now - start)
    return random_date


class RecoverPasswordFactory(factory.django.DjangoModelFactory):
    """Generates RecoverPassword instances for users who have requested a password
    reset. It assigns a User, a fake UUID as an email token, a requested date within
    the last 30 days, and an expiration date 5 days after the requested date"""

    class Meta:
        model = RecoverPassword

    user = factory.SubFactory(UserFactory)  # Use your UserFactory
    email_token = factory.Faker("uuid4")
    requested_date = factory.LazyFunction(random_datetime_last_30_days)
    expiration_date = factory.LazyAttribute(
        lambda o: o.requested_date + timedelta(days=5)
    )
