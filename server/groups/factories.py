# factories.py
import factory
from django.contrib.auth.models import User
from groups.models import ConsumerGroup, ConsumerGroupUsers, UserConsumerInvitation
from users.models import SupportedLocales,UserProfile
from factory import Faker

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # username = factory.LazyAttribute(lambda o: f"user_{o.sequence}_{factory.Faker('user_name').generate({})}")
    # username = factory.Sequence(lambda n: f"user_{n}_{factory.Faker('user_name').generate({})}")
    # username = factory.Sequence(lambda n: f"user_{n}_{factory.Faker('user_name')()}")
    # username = factory.Sequence(lambda n: f"user_{n}_{Faker('user_name').generate({})}")
    # username = factory.Sequence(lambda n: f"user_{n}_{factory.Faker('user_name').generate()}")
    # username = factory.LazyAttribute(lambda n: f"user_{n.sequence}_{factory.Faker('user_name')()}")
    # username = factory.LazyAttribute(lambda obj: f"user_{obj.__sequence}_{factory.Faker('user_name').generate({})}")
    # username = factory.LazyAttribute(lambda obj: f"user_{factory.Faker('user_name').evaluate(None, None, extra={})}_{obj.__sequence}")
    username = factory.Faker('user_name')
    email = factory.Faker('email')

class SupportedLocalesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SupportedLocales
        django_get_or_create = ('code',)  # This ensures existing locales are reused instead of created anew

    # Example locale codes. Adjust as necessary based on your actual locale codes.
    code = factory.Iterator(['en-us', 'fr-fr', 'es-es'])
    name = factory.LazyAttribute(lambda obj: f"Locale for {obj.code}")

class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    locale = factory.SubFactory(SupportedLocalesFactory)

class ConsumerGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ConsumerGroup

    nickname = factory.Faker('company')
    phone_number = factory.Faker('phone_number')
    postal_code = factory.Faker('postcode')
    street_name = factory.Faker('street_name')
    house_number = factory.Faker('building_number')
    neighborhood = factory.Faker('city')
    reference_location = factory.Faker('address')
    description = factory.Faker('text')


class ConsumerGroupUsersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ConsumerGroupUsers

    consumer_group = factory.SubFactory(ConsumerGroupFactory)
    user = factory.SubFactory(UserFactory)
    is_admin = factory.Faker('boolean')

class UserConsumerInvitationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserConsumerInvitation

    consumer_group = factory.SubFactory(ConsumerGroupFactory)
    inviting_user = factory.SubFactory(UserFactory)
    invited_user = factory.SubFactory(UserFactory)
    message = factory.Faker('sentence')
    status = factory.Iterator(['sent', 'accepted', 'declined'])
