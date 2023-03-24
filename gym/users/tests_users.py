from django.test import TestCase
from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase, Client




class TestUser(TestCase):

    def setUp(self):
        User.objects.create(
            username='Casper',
            email='user@example.com',
            password='string')
        User.objects.create(
            username='Muffin',
            email='user2@example.com',
            password='$geg54gegdfgf')

    def test_user(self):
        user_casper = User.objects.get(username='Casper')
        user_muffin = User.objects.get(username='Muffin')
        self.assertEqual(
            user_casper.username, "Casper")
        self.assertEqual(
            user_muffin.username, "Muffin")


client = Client()

class TestGetAllUsers(TestCase):

    def setUp(self):
        User.objects.create(
            username='Casper',
            email='user@example.com',
            password='string')
        User.objects.create(
            username='Muffin',
            email='user2@example.com',
            password='$geg54gegdfgf')

    def test_get_all_workout(self):

        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_get_one_workout(self):

        response = client.get('/api/users/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




##################################
class TestGetAllUsers_as_admin(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        self.client = APIClient()
        self.client.login(username='admin', password='admin123')
        User.objects.create(
            username='Casper',
            email='user@example.com',
            password='string')
        User.objects.create(
            username='Muffin',
            email='user2@example.com',
            password='$geg54gegdfgf')

    def test_get_all_workout(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_workout(self):
        response = self.client.get('/api/users/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
