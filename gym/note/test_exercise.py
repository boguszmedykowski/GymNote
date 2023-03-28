from django.test import TestCase
from note.models import Workout, Exercise

from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from .serializers import ExerciseSerializer
from django.test import RequestFactory




class TestGetOneExercise(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.workout_data = {
            'title': 'Test workout',
            'user': self.user,
        }
        self.workout = Workout.objects.create(**self.workout_data)
        self.exercise_data = {
            'title': 'Test exercise',
            'workout': self.workout,
        }
        self.exercise = Exercise.objects.create(**self.exercise_data)

    def test_get_valid_exercise(self):
        request = RequestFactory().get('/exercises/')
        serializer_context = {'request': request}
        serializer = ExerciseSerializer(instance=self.exercise, context=serializer_context)
        response = self.client.get(reverse('exercise-detail', kwargs={'pk': self.exercise.pk}))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_exercise(self):
        request = RequestFactory().get('/exercises/')
        serializer_context = {'request': request}
        response = self.client.get(reverse('exercise-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
