from typing import Any, Type

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile_from_user(
    sender: Type[User], instance: User, created: bool, **kwargs: Any
) -> None:
    """
    Automatically creates a UserProfile for a new User instance. If there is an issue
    in creating the UserProfile, the User instance is deleted.
    """
    if created:
        try:
            UserProfile.objects.create(user=instance)
        except Exception as e:
            instance.delete()  # Revert User creation in case of an error
            raise e


@receiver(pre_save, sender=User)
def check_email(sender: Type[User], instance: User, **kwargs: Any) -> None:
    email = instance.email
    if sender.objects.filter(email=email).exclude(username=instance.username).exists():
        raise ValidationError("Email Already Exists")
