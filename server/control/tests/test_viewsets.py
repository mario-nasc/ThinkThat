import jwt
from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from control.factories import UserFactory


class LoginViewTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory.create_batch(size=1, username='mario', password='password')
        self.url = self.url = reverse('control:login')
        self.data = {
            'username': self.user[0].username,
            'password': self.user[0].password
        }

    def test_login_success(self):
        response = self.client.post(self.url, self.data, HTTP_ACCEPT='application/json; version=1.0')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        header_data = jwt.get_unverified_header(response.data['token'])
        jwt_data = jwt.decode(
            response.data['token'],
            key=settings.SECRET_KEY,
            algorithms=[header_data['alg'], ]
        )
        self.assertEqual(jwt_data['username'], self.user[0].username)
