from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from ..models import User
from rest_framework import status


class TokenTests(APITestCase):
    def test_api_jwt(self):

        url = reverse('users:token_obtain_pair')
        u = User.objects.create_user(
            username='user', email='user@foo.com', password='pass')
        u.is_active = False
        u.save()

        resp = self.client.post(
            url, {'username': 'user@foo.com', 'password': 'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        resp = self.client.post(
            url, {'email': 'user@foo.com', 'password': 'pass'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']
        ref_token = resp.data['refresh']
        # print(token)

        verification_url = reverse('users:token_verify')
        resp = self.client.post(
            verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(
            verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

        url = reverse('hello')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'abc')
        resp = self.client.get(url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.get(url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # cheking for refresh token
        url = reverse('users:token_refresh')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + ref_token)
        resp = self.client.post(url, {'refresh': ref_token},
                           format='json')
        token = resp.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.post(
            verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
