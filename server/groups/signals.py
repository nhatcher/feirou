from django.db import transaction
from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from groups.models import ConsumerGroupUsers,ConsumerGroup
from django.core.exceptions import ValidationError

@receiver(post_save, sender=ConsumerGroup)
@transaction.atomic
def create_consumer_group_user_admin(sender, instance, created, **kwargs):
    """ Creating an adiming user in ConsumerGroupUsers"""
    if created:
        ConsumerGroupUsers.objects.create(consumer_group=instance, user=instance.user_creator, is_admin=True)


@receiver(pre_delete, sender=ConsumerGroupUsers)
@transaction.atomic
def ensure_at_least_one_admin_remains(sender, instance, **kwargs):
    # Check if the instance being deleted is an admin
    if instance.is_admin:
        # Count remaining admin users in the group, excluding the one being deleted
        remaining_admins = ConsumerGroupUsers.objects.filter(consumer_group=instance.consumer_group, is_admin=True).exclude(pk=instance.pk).count()
        if remaining_admins < 1:
            raise ValidationError("Cannot delete the last admin user from a Consumer Group.")