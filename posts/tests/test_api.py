from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.test import APITestCase, APIClient
from ..models import User
from rest_framework import status


class UserApiTest(APITestCase):

    def test_user_api(self):

        api_root = reverse('users:users-list')

        data = {'email': 'user@example.com', 'password': 'pass'}
        resp = self.client.post(
            api_root, data, format='json')

        url = reverse('users:token_obtain_pair')
        resp = self.client.post(
            url, data, format='json')
        token = resp.data['access']

        post_data = {
            "title": "test",
            "text": "some text"

        }
        # check create
        create_url = reverse('posts:posts-list')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        resp = self.client.post(
            create_url, post_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # check like
        like_url = reverse('posts:posts-like', kwargs={'pk': 1})
        resp = self.client.post(
            like_url, post_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        # count likes
        detail_url = reverse('posts:posts-detail', kwargs={'pk': 1})
        resp = self.client.get(detail_url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["total_likes"], 1)

        # count likes authors
        list_likes_list = reverse('posts:posts-fans', kwargs={'pk': 1})
        resp = self.client.get(list_likes_list, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)

        # check unlike
        unlike_url = reverse('posts:posts-unlike', kwargs={'pk': 1})
        resp = self.client.post(
            unlike_url, post_data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        detail_url = reverse('posts:posts-detail', kwargs={'pk': 1})
        resp = self.client.get(detail_url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["total_likes"], 0)
