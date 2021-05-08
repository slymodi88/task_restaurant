from django.contrib.auth.hashers import make_password
from django.test import TestCase

# Create your tests here.
from rest_framework import status

from user.models import User


class UserTestApi(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        create user in temp database to test the apis
        """
        User.objects.create(name='omar', employee_number='7412', password=make_password('123456'))

    def test_user_register_api(self):
        """
        test_user_register_api used to test the register api
        it takes the registration data and returns error if the test failed

        """
        url = "/api/user/register/"
        data = {

            'name': 'mohamd',
            'employee_number': '1245',
            'password': '123456',

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login_api(self):
        """
        test_user_login_api used to test the login api
        it takes the login data and returns error if the test failed

        """
        url = "/api/user/login/"
        data = {
            'name': 'omar',
            'employee_number': '7412',
            'password': '123456',

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_exist_api(self):
        """
        test_user_exist_api used to test the existing of a user in the database
        """
        url = "/api/user/register/"
        data = {

            'name': 'omar',
            'employee_number': '7412',
            'password': '123456',

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_not_exist_api(self):
        """

        test_user_not_exist_api used to test that only registered users in the database can login
        """
        url = "/api/user/login/"
        data = {

            'name': 'ali',
            'employee_number': '7895',
            'password': '123456',

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_wrong_password_api(self):
        """
        test_user_wrong_password_api to test the checking of  the password of the user trying to login

        """
        url = "/api/user/login/"
        data = {

            'name': 'omar',
            'employee_number': '7412',
            'password': '123455',

        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
