from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


# Create your tests here.

class UserSignalsProfileTest(TestCase):
    
    def test_user_signals_profile(self):

        user = User.objects.create_user(username='tester2024', password='passwordcheck')
        self.assertIsInstance(user.profile, Profile)
