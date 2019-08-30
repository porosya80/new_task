from .factories import UserFactory
from django.test import TestCase
from ..models import User




class UserTestCase(TestCase):
    def test_str(self):
        user = UserFactory()
        self.assertEqual(str(user), user.email)
