from django.test import TestCase
from users.models import User

from rest_framework import status
from django.test import TestCase, Client




class TestUser(TestCase):
    """ Test module for Workout model """

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
    """ Test module for GET all puppies API """

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