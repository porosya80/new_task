# import json
# from rest_framework import status
# from django.test import TestCase, Client
# from django.urls import reverse
# from ..models import User
# from ..serializers import UserSerializer
# # initialize the APIClient app
# client = Client()


# class GetAllUserTest(TestCase):

#     def setUp(self):
#        User.objects.create(
#            username="user1", first_name='vasil', last_name='pupkin', email='vasya@user.com')
#        User.objects.create(
#            username="user2", first_name='petro', last_name='vasechkin', email='petro@user.com')


#     def test_get_all_user(self):
#         response = client.get(reverse('UserViewSet'))
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
