from django.test import TestCase
from note.models import Workout
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .serializers import WorkoutSerializer



class TestWorkout(TestCase):
    """ Test module for Workout model """

    def setUp(self):
        Workout.objects.create(
            title='Casper',)
        Workout.objects.create(
            title='Muffin')

    def test_workout(self):
        workout_casper = Workout.objects.get(title='Casper')
        workout_muffin = Workout.objects.get(title='Muffin')
        self.assertEqual(
            workout_casper.title, "Casper")
        self.assertEqual(
            workout_muffin.title, "Muffin")


client = Client()

class TestGetAllWorkouts(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Workout.objects.create(
            title='Casper',)
        Workout.objects.create(
            title='Muffin')

    def test_get_all_workout(self):

        response = client.get('/api/workout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_workout(self):

        response = client.get('/api/workout/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)