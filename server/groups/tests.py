from django.test import TestCase
from models import ConsumerGroup 

class ConsumerGroupTests(TestCase):
    """Tests users API"""

    def setUp(self) -> None:
        """Sets up tests client."""
        # We create a user
        self.user = ConsumerGroup.objects.create_user(
            "my_username", "test@example.com", "A_Pas$word123"
        )