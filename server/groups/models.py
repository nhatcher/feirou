from django.db import models
from django.contrib.auth.models import User


class ConsumerGroup(models.Model):
    """
    A consumer group is a group of users that want to buy items.
    They can participate in any number of communities.
    """

    name = models.CharField(max_length=120, default="", unique=True)
    description = models.TextField()
    users = models.ManyToManyField(User)


class ProducerGroup(models.Model):
    """
    A consumer group is a group of users that want to buy items.
    They can participate in any number of communities.
    """

    name = models.CharField(max_length=120, default="", unique=True)
    description = models.TextField()
    users = models.ManyToManyField(User)


class Community(models.Model):
    """A community is where producer and consumer groups participate"""

    name = models.CharField(max_length=120, default="", unique=True)
    description = models.TextField()
    consumer_groups = models.ManyToManyField(ConsumerGroup)
    producer_groups = models.ManyToManyField(ProducerGroup)


class UserConsumerInvitations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(ConsumerGroup, on_delete=models.CASCADE)


class UserProducerInvitations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(ProducerGroup, on_delete=models.CASCADE)


class ConsumerGroupCommunityInvitation(models.Model):
    consumer = models.ForeignKey(ConsumerGroup, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)


class ProducerGroupCommunityInvitation(models.Model):
    producer = models.ForeignKey(ProducerGroup, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)