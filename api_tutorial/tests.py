import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api_tutorial.factories import UserFactory


class RegisterUserTestCase(APITestCase):
    """
    Test the ability of users to sign up for new accounts
    """

    def test_create_user(self):
        """Sign up for a new account"""
        response = self.client.post(
            reverse('user-list'),
            json.dumps(UserFactory.stub().__dict__),
            content_type='application/json'
        )
        stored_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, u'The new user was not created.')
        self.assertNotIn('password', stored_data)
        self.assertFalse(stored_data.get('is_active'))
        self.assertFalse(stored_data.get('is_superuser'))

    def test_bad_request(self):
        """Sign up with missing information should fail"""
        userStub = UserFactory.stub().__dict__
        userStub.pop('username')
        response = self.client.post(
            reverse('user-list'),
            json.dumps(userStub),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, u'The request was valid.')


class RetrieveUserTestCase(APITestCase):
    def test_get_user(self):
        """Get existing user"""
        user = UserFactory()

        response = self.client.get(
            reverse('user-detail', kwargs={'pk': user.pk}),
            content_type='application/json'
        )
        stored_data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.email, stored_data.get('email'))
        self.assertEqual(user.username, stored_data.get('username'))
        self.assertEqual(user.first_name, stored_data.get('first_name'))
        self.assertEqual(user.last_name, stored_data.get('last_name'))

    def test_get_invalid_user(self):
        """Try to fetch an invalid user"""
        response = self.client.get(
            reverse('user-detail', kwargs={'pk': 1000}),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
