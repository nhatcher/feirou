# generate_fixtures.py
import os
import sys
import django
import json
from random import choice
from django.core.serializers import serialize

"""
This script automatically generates test data for the Django models related to consumer groups, 
including ConsumerGroup, ConsumerGroupUsers, and UserConsumerInvitation models. It utilizes 
Factory Boy to create instances of these models and then serializes the generated data to JSON files.

These JSON files can be used as fixtures for loading test data into the Django test database, 
facilitating testing by providing a consistent and reusable set of data for test cases.

Usage:
    Run this script from the command line to generate the JSON fixture files. Ensure that the Django
    environment is properly set up and that the Factory Boy definitions for the models are correctly 
    implemented in your Django app.

    $ python generate_fixtures.py

Output:
    The script will generate three JSON files in the current directory:
    - consumer_groups.json: Contains test data for the ConsumerGroup model.
    - consumer_group_users.json: Contains test data for the ConsumerGroupUsers model.
    - user_consumer_invitations.json: Contains test data for the UserConsumerInvitation model.

"""

deployment_scripts_dir = os.path.dirname(os.path.abspath(__file__))
fake_data_dir = os.path.join(deployment_scripts_dir,'fake_data')

feirou_dir = os.path.dirname(deployment_scripts_dir)
sys.path.append(os.path.join(feirou_dir,'server'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings.development")
django.setup()

from groups.factories import SupportedLocalesFactory, UserFactory, UserProfileFactory, ConsumerGroupFactory, ConsumerGroupUsersFactory, UserConsumerInvitationFactory

users_path = os.path.join(fake_data_dir, 'users.json')
consumer_groups_path = os.path.join(fake_data_dir, 'consumer_groups.json')
consumer_group_users_path = os.path.join(fake_data_dir, 'consumer_group_users.json')
user_consumer_invitations_path = os.path.join(fake_data_dir, 'user_consumer_invitations.json')
def generate_data():

    # Generate supported locales (if needed)
    locales = [SupportedLocalesFactory.create() for _ in range(2)]

    # Generate user profiles (which also generates users)
    user_profiles = [UserProfileFactory.create() for _ in range(20)]
    users = [profile.user for profile in user_profiles]  # Extract the User instances from the generated profiles

    # Generate Consumer Groups
    consumer_groups = [ConsumerGroupFactory.create() for _ in range(10)]

    # Generate ConsumerGroupUsers with associations
    consumer_group_users = [ConsumerGroupUsersFactory.create(consumer_group=choice(consumer_groups), user=choice(users)) for _ in range(20)]

    # Generate UserConsumerInvitations with associations
    user_consumer_invitations = []
    for _ in range(20):
        inviting_user = choice(users)
        invited_user = choice([user for user in users if user != inviting_user])
        consumer_group = choice(consumer_groups)
        invitation = UserConsumerInvitationFactory.create(consumer_group=consumer_group, inviting_user=inviting_user, invited_user=invited_user)
        user_consumer_invitations.append(invitation)

    # Serialize and save data in JSON file
    with open(users_path, 'w') as cg_file:
        json.dump(json.loads(serialize('json', users)), cg_file)

    with open(consumer_groups_path, 'w') as cg_file:
        json.dump(json.loads(serialize('json', consumer_groups)), cg_file)

    with open(consumer_group_users_path, 'w') as cgu_file:
        json.dump(json.loads(serialize('json', consumer_group_users)), cgu_file)

    with open(user_consumer_invitations_path, 'w') as uci_file:
        json.dump(json.loads(serialize('json', user_consumer_invitations)), uci_file)

if __name__ == "__main__":
    generate_data()
