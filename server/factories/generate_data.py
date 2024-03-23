"""
This script generates test data for Django models using Factory Boy and exports the 
data to JSON files.

The script performs the following steps:
1. Flushes the current database to start with a clean slate.
2. Generates instances for supported locales, users, user profiles, pending users, recover 
passwords.
3. Exports the generated instances to JSON files for future use as fixtures or for testing 
purposes.
"""

import json
import os
import random
import sys

import django
from django.core.management import call_command
from django.core.serializers import serialize
from django.db.models.signals import post_save

# Setting up the environment paths and Django settings
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURES_DIR = os.path.join(PROJECT_PATH, "fixtures")
sys.path.append(PROJECT_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.development")
django.setup()

from django.contrib.auth.models import User

# Importing Factory definitions and models
from factory_users import (
    PendingUserFactory,
    RecoverPasswordFactory,
    SupportedLocalesFactory,
    UserFactory,
    UserProfileFactory,
)
from users.signals import create_user_profile_from_user

# Clearing the database
call_command("flush", "--noinput")


def create_user_profile(users, locales):
    """Generates user profiles associated with randomly chosen locales."""
    user_profiles = []
    for user in users:
        locale = random.choice(locales)
        user_profile = UserProfileFactory.create(user=user, locale=locale)
        user_profiles.append(user_profile)

    return user_profiles


def create_pending_user(user_profiles):
    """Generates pending users for user profiles with inactive users."""
    pending_users = []
    for user_profile in user_profiles:
        if not user_profile.user.is_active:
            pending_user = PendingUserFactory.create(user_profile=user_profile)
            pending_users.append(pending_user)

    return user_profiles


def create_recover_password(users, n_users):
    """Generates password recovery instances for a sample of users."""
    users = random.sample(users, n_users)

    recover_passwords = []
    for user in users:
        recover_password = RecoverPasswordFactory.create(user=user)
        recover_passwords.append(recover_password)

    return recover_passwords


def generate_data(fixtures_dir):
    """Main function to generate all data and export to JSON files."""
    # Generate supported locales
    supported_locales = [SupportedLocalesFactory.create() for _ in range(2)]

    # Generate users
    post_save.disconnect(create_user_profile_from_user, sender=User)
    user = [UserFactory.create() for _ in range(20)]

    # Generate user profiles
    user_profile = create_user_profile(user, supported_locales)

    # Generate pending user
    pending_user = create_pending_user(user_profile)

    # Generate recover password
    recover_password = create_recover_password(user, 5)

    # Exporting users - data
    app_models = "users"
    data_to_write = {
        "user.json": user,
        "supported_locales.json": supported_locales,
        "user_profile.json": user_profile,
        "pending_user.json": pending_user,
        "recover_password.json": recover_password,
    }

    for file_name, data in data_to_write.items():
        file_path = os.path.join(fixtures_dir, app_models, file_name)
        with open(file_path, "w") as file:
            json.dump(json.loads(serialize("json", data)), file)


if __name__ == "__main__":
    generate_data(FIXTURES_DIR)
    print("Success: data created! ")
