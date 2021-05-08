import datetime

from django.contrib.auth.hashers import make_password
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import status

from tables.models import Reservation, Table, WorkingHour
from user.models import User


class TableReservationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        create user in temp database to test the apis
        """
        user = User.objects.create(name='omar', employee_number='7412', password=make_password('123456'))
        User.objects.create_token(user)
        Table.objects.create(table_num=1, num_seats=2)
        WorkingHour.objects.create(start_day='12:00', end_day='23:59')
        Table.objects.create(table_num=1, num_seats=2)
        Reservation.objects.create(start_time='15:30', end_time='17:35', table=Table.objects.get(id=1))

    def test_reservation_post_api(self):
        url = "/api/reservations/"
        data = {

            'start_time': '15:30',
            'end_time': '16:40',
            'table': '1',
        }

        user_token = User.objects.first().token
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + user_token
        }
        response = self.client.post(url, data, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reservation_get_api(self):
        url = "/api/reservations/"

        user_token = User.objects.first().token
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + user_token
        }
        response = self.client.get(url, format='json', **headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reservation_delete_api(self):
        url = "/api/reservations/1"

        user_token = User.objects.first().token
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + user_token
        }
        response = self.client.delete(url, format='json', **headers)

        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_reservation_available_get_api(self):
        url = "/api/reservations/available/?num_seats=2"

        user_token = User.objects.first().token
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + user_token
        }
        response = self.client.get(url, format='json', **headers)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

