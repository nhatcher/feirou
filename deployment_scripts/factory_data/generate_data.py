"""
This script generates test data for Django models using Factory Boy and exports the data to JSON files.

The script performs the following steps:
1. Flushes the current database to start with a clean slate.
2. Generates instances for supported locales, users, user profiles, pending users, recover passwords, consumer groups, consumer group users, and user consumer invitations.
3. Exports the generated instances to JSON files for future use as fixtures or for testing purposes.

Usage:
Run this script from the command line within the Django environment:
$ python generate_fixtures.py
"""

import os
import sys
import django
import json
import random
from django.core.serializers import serialize
from django.db.models.signals import post_save
from django.core.management import call_command

# Setting up the environment paths and Django settings
DEPLOYMENT_SCRIPTS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FACTORY_DATA_DIR = os.path.join(DEPLOYMENT_SCRIPTS_DIR, 'factory_data')
FAKE_DATA_DIR = os.path.join(FACTORY_DATA_DIR, 'data')
sys.path.append(FACTORY_DATA_DIR)

FEIROU_DIR = os.path.dirname(DEPLOYMENT_SCRIPTS_DIR)
PROJECT_PATH = os.path.join(FEIROU_DIR, 'server')
sys.path.append(PROJECT_PATH)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.development")
django.setup()

# Importing Factory definitions and models
from factory_user import SupportedLocalesFactory, UserFactory, UserProfileFactory, PendingUserFactory, RecoverPasswordFactory
from factory_groups import ConsumerGroupFactory, ConsumerGroupUsersFactory, UserConsumerInvitationFactory
from users.models import update_profile_signal
from django.contrib.auth.models import User

# Clearing the database
call_command('flush', '--noinput')

def create_user_profile(users,locales):
    """Generates user profiles associated with randomly chosen locales."""
    user_profiles = []
    for user in users:
        locale = random.choice(locales)
        user_profile = UserProfileFactory.create(user= user,locale = locale)
        user_profiles.append(user_profile)

    return user_profiles

def create_pending_user(user_profiles):
    """Generates pending users for user profiles with inactive users."""
    pending_users = []
    for user_profile in user_profiles:
        if not user_profile.user.is_active:
            pending_user = PendingUserFactory.create(user_profile= user_profile)
            pending_users.append(pending_user)

    return user_profiles

def create_recover_password(users,n_users):
    """Generates password recovery instances for a sample of users."""
    users = random.sample(users, n_users)

    recover_passwords = []
    for user in users:
        recover_password = RecoverPasswordFactory.create(user = user)
        recover_passwords.append(recover_password)

    return recover_passwords

def create_consumer_group_user(users,consumer_groups,n_instace):
    """Generates consumer group users ensuring unique user-consumer group pairs."""
    used_pairs = set()
    consumer_group_users = []

    for _ in range(n_instace - 1):
        while True:
            consumer_group = random.choice(consumer_groups)
            user = random.choice(users)
            pair = (consumer_group.id, user.id)

            if pair not in used_pairs:
                consumer_group_user = ConsumerGroupUsersFactory.create(consumer_group=consumer_group, user=user)
                consumer_group_users.append(consumer_group_user)
                used_pairs.add(pair)
                break
    
    return consumer_group_users

def create_user_consumer_invitation(users,consumer_groups):
    """Generates user consumer invitations with random inviting and invited users."""
    user_consumer_invitations = []
    for _ in range(20):
        inviting_user = random.choice(users)
        invited_user = random.choice([user for user in users if user != inviting_user])
        consumer_group = random.choice(consumer_groups)
        invitation = UserConsumerInvitationFactory.create(consumer_group=consumer_group, inviting_user=inviting_user, invited_user=invited_user)
        user_consumer_invitations.append(invitation)

    return user_consumer_invitations

def generate_data(fake_data_dir):
    """Main function to generate all data and export to JSON files."""
    # Generate supported locales
    locales = [SupportedLocalesFactory.create() for _ in range(2)]

    # Generate users
    post_save.disconnect(update_profile_signal, sender=User)
    user = [UserFactory.create() for _ in range(20)]
    
    # Generate user profiles
    user_profile = create_user_profile(user,locales)
    
    # Generate pending user
    pending_user = create_pending_user(user_profile)
    
    # Generate recover password
    recover_password = create_recover_password(user,5)
    
    # Generate consumer groups
    consumer_group = [ConsumerGroupFactory.create() for _ in range(10)]
    
    # Generate consumer group users
    consumer_group_user = create_consumer_group_user(user,consumer_group,20)

    # Generate UserConsumerInvitations
    user_consumer_invitation = create_user_consumer_invitation(user,consumer_group)

    # Exporting data
    data_to_write = {
        'users.json': user,
        'user_profile.json': user_profile,
        'pending_user.json': pending_user,
        'recover_password.json': recover_password,
        'consumer_group.json': consumer_group,
        'consumer_group_user.json': consumer_group_user,
        'user_consumer_invitation.json': user_consumer_invitation,
    }

    for file_name, data in data_to_write.items():
        file_path = os.path.join(fake_data_dir, file_name)
        with open(file_path, 'w') as file:
            json.dump(json.loads(serialize('json', data)), file)


if __name__ == "__main__":
    generate_data(FAKE_DATA_DIR)
