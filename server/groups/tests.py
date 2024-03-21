from django.test import TestCase
from django.db.models.signals import post_save
from groups.models import ConsumerGroup, ConsumerGroupUsers
from factories.factory_groups import ConsumerGroupFactory
from users.models import update_profile_signal
from django.contrib.auth.models import User
from django.core.management import call_command
from groups.signals import create_consumer_group_user_admin
from django.core.exceptions import ValidationError
from django.db import transaction

class ConsumerGroupTests(TestCase):

    disconnected_signals = []

    def setUp(self):
        # Disconnect the signal
        self.disconnected_signals.append((update_profile_signal, User, post_save))
        self.disconnected_signals.append((create_consumer_group_user_admin, ConsumerGroup, post_save))
        for receiver, sender, signal in self.disconnected_signals:
            signal.disconnect(receiver, sender=sender)

        # Manually load fixtures
        call_command(
            "loaddata",
            "consumer_group.json",
            "consumer_group_user.json",
            "pending_user.json",
            "recover_password.json",
            "supported_locales.json",
            "user_consumer_invitation.json",
            "user.json",
            "user_profile.json",
        )

        # Reconnect the signals
        for receiver, sender, signal in self.disconnected_signals:
            signal.connect(receiver, sender=sender)

    def test_consumer_group_creation(self):
        """Test the creation of a ConsumerGroup."""
        # Create a test user who will be the creator of the ConsumerGroup
        user_creator = User.objects.create_user(username='testuser', password='12345')
        ConsumerGroupFactory.create(nickname="Test Group",user_creator = user_creator)
        self.assertTrue(ConsumerGroup.objects.filter(nickname="Test Group").exists())

    def test_consumer_group_deletion(self):
        """Test ConsumerGroup deletion and its effect on related models."""
        # Fetch an existing ConsumerGroup instance from the database
        consumer_group = ConsumerGroup.objects.first()
        if not consumer_group:
            self.fail("No ConsumerGroup instances available in the test database.")

        # Store the ID before deletion for later checks
        consumer_group_id = consumer_group.id

        # Check pre-conditions to ensure the fixture data includes associated ConsumerGroupUsers
        self.assertTrue(
            ConsumerGroupUsers.objects.filter(consumer_group=consumer_group).exists()
        )

        # Delete the consumer_group
        consumer_group.delete()

        # Verify the ConsumerGroup instance is deleted
        self.assertFalse(ConsumerGroup.objects.filter(id=consumer_group_id).exists())

        # Verify related ConsumerGroupUsers are also handled as expected (e.g., deleted or set to null, depending on your model's ON_DELETE behavior)
        self.assertFalse(
            ConsumerGroupUsers.objects.filter(
                consumer_group_id=consumer_group_id
            ).exists()
        )

    def test_creator_is_registered_as_admin_on_group_creation(self):
        # Create a test user who will be the creator of the ConsumerGroup
        user_creator = User.objects.create_user(username='testuser', password='12345')

        # Create a ConsumerGroup instance with the test user as the creator
        new_group = ConsumerGroup.objects.create(nickname='Test Group', user_creator=user_creator)

        # Check that a ConsumerGroupUsers instance exists for this group and user, and that is_admin is True
        self.assertTrue(ConsumerGroupUsers.objects.filter(consumer_group=new_group, user=user_creator, is_admin=True).exists(), "The creator was not registered as an admin for the new ConsumerGroup")

    def test_prevent_last_admin_deletion(self):
        # Find a ConsumerGroup that contains only one admin user in ConsumerGroupUsers
        for group in ConsumerGroup.objects.all():
            admin_users = ConsumerGroupUsers.objects.filter(consumer_group=group, is_admin=True)
            if admin_users.count() == 1:
                single_admin = admin_users.first()
                break
        else:
            self.fail("No ConsumerGroup with a single admin user found for testing.")

        # Attempt to delete this admin user, expecting an error
        with self.assertRaises(ValidationError), transaction.atomic():
            single_admin.delete()

        # Ensure the admin user still exists
        self.assertTrue(ConsumerGroupUsers.objects.filter(pk=single_admin.pk).exists(), "Admin user was unexpectedly deleted.")

