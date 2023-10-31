"""
This module defines factories for the ConsumerGroup, ConsumerGroupUsers, and UserConsumerInvitation models using Factory Boy.
"""
import factory
from groups.models import ConsumerGroup, ConsumerGroupUsers, UserConsumerInvitation
from factories.factory_user import UserFactory

class ConsumerGroupFactory(factory.django.DjangoModelFactory):
    """Generates fake instances with attributes like nickname, phone number, postal code, and more, using Faker providers for realistic but randomized data"""

    class Meta:
        model = ConsumerGroup

    user_creator = factory.SubFactory(UserFactory)
    nickname = factory.Faker('company')
    phone_number = factory.Faker('phone_number')
    postal_code = factory.Faker('postcode')
    street_name = factory.Faker('street_name')
    house_number = factory.Faker('building_number')
    neighborhood = factory.Faker('city')
    reference_location = factory.Faker('address')
    description = factory.Faker('text')

class ConsumerGroupUsersFactory(factory.django.DjangoModelFactory):
    """Produces instances that represent the association between users and consumer groups. It assigns a ConsumerGroup and a User to each instance, with a boolean indicating if the user is an admin within the group."""
    class Meta:
        model = ConsumerGroupUsers

    consumer_group = factory.SubFactory(ConsumerGroupFactory)
    user = factory.SubFactory(UserFactory)
    is_admin = factory.Faker('boolean')

class UserConsumerInvitationFactory(factory.django.DjangoModelFactory):
    """Creates instances to simulate invitations sent to users to join specific consumer groups."""

    class Meta:
        model = UserConsumerInvitation

    consumer_group = factory.SubFactory(ConsumerGroupFactory)
    inviting_user = factory.SubFactory(UserFactory)
    invited_user = factory.SubFactory(UserFactory)
    message = factory.Faker('sentence')
    status = factory.Iterator(['sent', 'accepted', 'declined'])
