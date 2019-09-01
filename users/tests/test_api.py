from rest_framework.reverse import reverse ,reverse_lazy
from rest_framework.test import APITestCase, APIClient
from ..models import User
from rest_framework import status


class UserApiTest(APITestCase):

    def test_user_api(self):

        api_root = reverse('users:users-list')

        data = {'email': 'user@example.com', 'password': 'pass'}

        resp = self.client.post(
            api_root, data , format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        url = reverse('users:token_obtain_pair')
        resp = self.client.post(
            url, data , format='json')
        token = resp.data['access']

        verification_url = reverse('users:token_verify')
        resp = self.client.post(
            verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
