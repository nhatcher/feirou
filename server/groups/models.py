from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User

class ConsumerGroup(models.Model):
    """
    Represents a Consumer Group, which can be an individual user or a group of users interested in purchasing items. 
    This entity is capable of participating in various communities. Each Consumer Group is characterized by 
    personal and contact information, along with a unique logo and a descriptive text.
    """
    nickname = models.CharField(max_length=100)  # Nickname of the Consumer Group
    phone_number = models.CharField(max_length=15)  # Contact phone number
    postal_code = models.CharField(max_length=10)  # Postal code for the location
    street_name = models.CharField(max_length=255)  # Name of the street
    house_number = models.CharField(max_length=10)  # House or business number, accepting alphanumeric values
    neighborhood = models.CharField(max_length=100)  # Name of the neighborhood
    reference_location = models.TextField(blank=True, null=True)  # Additional reference location, optional
    logo = models.ImageField(upload_to='consumer_logos/')  # Logo image, requires MEDIA_ROOT and MEDIA_URL configurations
    description = models.TextField()  # Descriptive text about the Consumer Group

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update of the record

    def __str__(self):
        return self.nickname

class ConsumerGroupUsers(models.Model):
    """
    Defines the association between users and their respective Consumer Group, including a flag to indicate 
    if a user holds administrative privileges within the group. This model helps in organizing the roles and 
    memberships of users within Consumer Groups.
    """
    consumer_group = models.ForeignKey(ConsumerGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField()  # Indicates whether the user is an admin of the Consumer Group

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["consumer_group", "user"],  # Corrected field name from "consumer_group" to "consumer_group"
                name="unique_consumer_group_user",
            )
        ]

class UserConsumerInvitation(models.Model):
    """
    Manages the invitations sent to users to join specific Consumer Unities. This model ensures each invitation is
    unique to a user-consumer group pair, preventing duplicate invitations. It tracks the invitation status and
    allows for a personalized message.
    """
    consumer_group = models.ForeignKey(ConsumerGroup, on_delete=models.CASCADE)
    inviting_user = models.ForeignKey(User, related_name='sent_consumer_invitations', on_delete=models.CASCADE)
    invited_user = models.ForeignKey(User, related_name='received_consumer_invitations', on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)  # Optional personalized message
    status = models.CharField(max_length=10, choices=[('sent', 'Sent'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='sent')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["consumer_group", "inviting_user", "invited_user"],
                name="unique_user_consumer_invitation",
            )
        ]

class ProductionType(models.Model):
    name = models.CharField(max_length=20, choices=[
        ("agricultural", "Agricultural"),
        ("handicraft", "Handicraft"),
        ("industrial", "Industrial"),
        ("artisanal_food", "Artisanal Food Production"),
    ])

    def __str__(self):
        return self.name
    
class ProducerGroup(models.Model):
    """
    Represents a Producer Group, which is typically a collection of producers or a single producer
    engaged in the creation or supply of goods. This entity can be associated with various types of
    production and might participate in different communities or associations. Each Producer Group is
    characterized by a trade name, contact information, and potentially an association name. The model
    also captures the group's production method and types, offering insights into their practices and
    specialties.
    """

    trade_name = models.CharField(max_length=100)  # String for the trade name
    document_number = models.CharField(max_length=20)  # String for the document number
    phone_number = models.CharField(max_length=15)  # String for the phone number
    postal_code = models.CharField(max_length=10)  # String for the postal code
    street_name = models.CharField(max_length=255)  # String for the street name
    house_number = models.CharField(max_length=10)  # House or business number, accepting alphanumeric values
    neighborhood = models.CharField(max_length=100)  # String for the neighborhood
    reference_location = models.TextField(blank=True, null=True)  # Optional text for a reference location
    email = models.EmailField()  # Email field
    association_name = models.CharField(max_length=100, blank=True, null=True)  # Optional string for association name
    logo = models.ImageField(upload_to='producer_logos/')  # Image for the logo

    # Choices for production type
    production_types = models.ManyToManyField(ProductionType, related_name='producers')

    # Choices for production method
    PRODUCTION_METHOD_CHOICES = [
        ("conventional", "Conventional"),
        ("agroecology", "Agroecological"),
        ("in_transition", "In transition to agroecological"),
        ("organic_cert", "Organic (certified)"),
        ("other", "Other"),
    ]
    production_method = models.CharField(max_length=20, choices=PRODUCTION_METHOD_CHOICES)

    description = models.TextField()  # Text field for presentation

    def __str__(self):
        return self.trade_name

class ProducerGroupUsers(models.Model):
    """
    Defines the association between users and their respective Producer Group, including a flag to indicate 
    if a user holds administrative privileges within the group. This model helps in organizing the roles and 
    memberships of users within Producer Groups.
    """
    producer_group = models.ForeignKey(ProducerGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField()  # Indicates whether the user is an admin of the Producer Group

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["producer_group", "user"],  # Corrected field name from "producer_group" to "producer_group"
                name="unique_producer_group_user",
            )
        ]

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
    email = models.EmailField()  # Email field
    association_name = models.CharField(max_length=100, blank=True, null=True)  # Optional string for association name
    logo = models.ImageField(upload_to='community_logos/')  # Image for the logo
    presentation = models.TextField()  # Text field for presentation
    bylaws = models.FileField(upload_to='community_bylaws/', blank=True, null=True)  # Optional file for bylaws
    letter_of_principles = models.FileField(upload_to='community_principles/', blank=True, null=True)  # Optional file for letter of principles

    def __str__(self):
        return self.trade_name

class UserProducerInvitations(models.Model):
    """
    Manages the invitations sent to users to join specific Producer Group. This model ensures each invitation is
    unique to a user-produce group pair, preventing duplicate invitations. It tracks the invitation status and
    allows for a personalized message.
    """
    producer_group = models.ForeignKey(ProducerGroup, on_delete=models.CASCADE)
    inviting_user = models.ForeignKey(User, related_name='sent_producer_invitations', on_delete=models.CASCADE)
    invited_user = models.ForeignKey(User, related_name='received_producer_invitations', on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)  # Optional personalized message
    status = models.CharField(max_length=10, choices=[('sent', 'Sent'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='sent')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["producer_group", "inviting_user", "invited_user"],
                name="unique_user_producer_invitation",
            )
        ]


class ConsumerGroupCommunityInvitation(models.Model):
    consumer = models.ForeignKey(ConsumerGroup, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)


class ProducerGroupCommunityInvitation(models.Model):
    producer = models.ForeignKey(ProducerGroup, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)


class PlatformType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class GenericSocialLink(models.Model):
    # This field will point to the model (ProducerGroup, Community, etc.)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    platform_type = models.ForeignKey(PlatformType, on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        unique_together = ('content_type', 'object_id', 'platform_type')

    def __str__(self):
        return f"{self.platform_type.name} link for {self.content_object}"