from django.test import TestCase
from .models import User


class UserTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        User.objects.create(
            username="user1", first_name='vasil', last_name='pupkin', email='vasya@user.com')
        User.objects.create(
            username="user2", first_name='petro', last_name='vasechkin', email='petro@user.com')

    def test_user_model(self):
        user_vasya = User.objects.get(username='user1')
        user_petya = User.objects.get(username='user2')
        self.assertEqual(
            user_vasya.__str__(), "vasya@user.com")
        self.assertEqual(
            user_petya.__str__(), "petro@user.com")
