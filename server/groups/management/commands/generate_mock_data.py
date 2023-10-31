from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
import logging
from random import randint

from groups.models import Community, ConsumerGroup, ProducerGroup

logger = logging.getLogger("faker")
logger.setLevel(logging.INFO)  # Quiet faker locale messages down in tests.

fake = Faker("en_US")


def generate_consumers_groups(n, community_count):
    for _ in range(0, n):
        name = fake.word()
        description = fake.text()
        group = ConsumerGroup.objects.create(name=name, description=description)
        community_pk = randint(1, community_count)
        Community.objects.get(id=community_pk).consumer_groups.add(group)


def generate_producers_groups(n, community_count):
    for _ in range(0, n):
        name = fake.word()
        description = fake.text()
        group = ProducerGroup.objects.create(name=name, description=description)
        community_pk = randint(1, community_count)
        Community.objects.get(id=community_pk).producer_groups.add(group)


def generate_communities(n=3):
    for _ in range(0, n):
        name = fake.word()
        description = fake.text()
        Community.objects.create(name=name, description=description)


def generate_users(user_count, p_group_count, c_group_count):
    with open('passwords.txt', 'w') as f:
        for _ in range(0, user_count):
            username = fake.unique.user_name()
            email_address = fake.unique.email()
            password = fake.password()
            first_name = fake.first_name()
            last_name = fake.last_name()
            f.write(f"{username} {password}\n")

            user = User.objects.create_user(
                username,
                email_address,
                password,
                first_name=first_name,
                last_name=last_name,
            )
            n = randint(0, 4)
            for _ in (0, n):
                state = randint(0, p_group_count + c_group_count - 1)
                if state < p_group_count:
                    group = ProducerGroup.objects.get(id=state+1)
                    group.users.add(user)
                else:
                    group = ConsumerGroup.objects.get(id=state-p_group_count+1)
                    group.users.add(user)


class Command(BaseCommand):
    def handle(self, **options):
        user_count = 30
        p_group_count = 5
        c_group_count = 4
        community_count = 3
        generate_communities(community_count)
        generate_producers_groups(p_group_count, community_count)
        generate_consumers_groups(c_group_count, community_count)
        generate_users(user_count, p_group_count, c_group_count)
