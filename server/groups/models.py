from django.db import models
from django.contrib.auth.models import User


class ConsumerGroup(models.Model):
    """
    A consumer group is a group of users that want to buy items.
    They can participate in any number of communities.
    """

    nickname = models.CharField(max_length=100)  # String for nickname
    users = models.ManyToManyField(User)
    users_admin = models.ManyToManyField(User)
    document_number = models.CharField(max_length=20)  # String for document number, assuming it's something like a social security number or a business identification number
    phone_number = models.CharField(max_length=15)  # String for phone number
    postal_code = models.CharField(max_length=10)  # String for postal code
    street_name = models.CharField(max_length=255)  # String for street name
    number = models.CharField(max_length=10)  # String for house/business number, could be an IntegerField, but we use CharField to accept numbers like '12A'
    neighborhood = models.CharField(max_length=100)  # String for neighborhood
    reference_location = models.TextField(blank=True, null=True)  # Optional text for a reference location
    gps_location = models.CharField(max_length=255)  # String for GPS location, could be formatted as 'latitude, longitude'
    logo = models.ImageField(upload_to='consumer_logos/')  # Image for the logo, MEDIA_ROOT and MEDIA_URL need to be configured in settings.py to work properly
    presentation = models.TextField()  # Text field for presentation

    def __str__(self):
        return self.nickname


class ProducerGroup(models.Model):
    """
    A consumer group is a group of users that want to buy items.
    They can participate in any number of communities.
    """

    trade_name = models.CharField(max_length=100)  # String for the trade name
    users = models.ManyToManyField(User)
    users_admin = models.ManyToManyField(User)
    document_number = models.CharField(max_length=20)  # String for the document number
    phone_number = models.CharField(max_length=15)  # String for the phone number
    postal_code = models.CharField(max_length=10)  # String for the postal code
    street_name = models.CharField(max_length=255)  # String for the street name
    neighborhood = models.CharField(max_length=100)  # String for the neighborhood
    reference_location = models.TextField(blank=True, null=True)  # Optional text for a reference location
    gps_location = models.CharField(max_length=255)  # String for the GPS location, formatted as 'latitude, longitude'
    email = models.EmailField()  # Email field
    instagram = models.URLField(blank=True, null=True)  # Optional URL field for Instagram
    facebook = models.URLField(blank=True, null=True)  # Optional URL field for Facebook
    site = models.URLField(blank=True, null=True)  # Optional URL field for website
    association_name = models.CharField(max_length=100, blank=True, null=True)  # Optional string for association name
    logo = models.ImageField(upload_to='producer_logos/')  # Image for the logo

    # Choices for production type
    PRODUCTION_TYPE_CHOICES = [
        ("agricultural", "Agricultural"),
        ("handicraft", "Handicraft"),
    ]
    production_type = models.CharField(max_length=20, choices=PRODUCTION_TYPE_CHOICES)

    # Choices for production method
    PRODUCTION_METHOD_CHOICES = [
        ("conventional", "Conventional"),
        ("agroecology", "Agroecological"),
        ("in_transition", "In transition to agroecological"),
        ("organic_cert", "Organic (certified)"),
        ("other", "Other"),
    ]
    production_method = models.CharField(max_length=20, choices=PRODUCTION_METHOD_CHOICES)

    presentation = models.TextField()  # Text field for presentation

    def __str__(self):
        return self.trade_name


class Community(models.Model):
    """A community is where producer and consumer groups participate"""

    trade_name = models.CharField(max_length=100)  # String for the trade name
    consumer_groups = models.ManyToManyField(ConsumerGroup)
    producer_groups = models.ManyToManyField(ProducerGroup)
    users_admin = models.ManyToManyField(User)
    document_number = models.CharField(max_length=20)  # String for the document number
    phone_number = models.CharField(max_length=15)  # String for the phone number
    postal_code = models.CharField(max_length=10)  # String for the postal code
    street_name = models.CharField(max_length=255)  # String for the street name
    neighborhood = models.CharField(max_length=100)  # String for the neighborhood
    reference_location = models.TextField(blank=True, null=True)  # Optional text for a reference location
    gps_location = models.CharField(max_length=255)  # String for the GPS location, formatted as 'latitude, longitude'
    email = models.EmailField()  # Email field
    instagram = models.URLField(blank=True, null=True)  # Optional URL field for Instagram
    facebook = models.URLField(blank=True, null=True)  # Optional URL field for Facebook
    site = models.URLField(blank=True, null=True)  # Optional URL field for website
    association_name = models.CharField(max_length=100, blank=True, null=True)  # Optional string for association name
    logo = models.ImageField(upload_to='community_logos/')  # Image for the logo
    bylaws = models.FileField(upload_to='community_bylaws/', blank=True, null=True)  # Optional file for bylaws
    letter_of_principles = models.FileField(upload_to='community_principles/', blank=True, null=True)  # Optional file for letter of principles

    def __str__(self):
        return self.trade_name


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