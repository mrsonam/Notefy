from django.test import TestCase
from .models import ApiModel

# Create your tests here.
class TestApi(TestCase):

    def setUp(self):
        
        self.user1 = ApiModel.objects.create(
            user_name = "mrsonam",
            user_address = "Boudha",
            user_contact = 9803508744
        )
    
    def test_check_address(self):
        user = ApiModel.objects.get(user_name="mrsonam")
        value = user.user_address
        self.assertEquals(value, "Boudha")
