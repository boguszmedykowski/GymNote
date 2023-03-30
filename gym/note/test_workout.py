from django.test import TestCase
from note.models import Workout

from rest_framework import status
from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from .serializers import WorkoutSerializer
from django.test import RequestFactory




class TestGetOneWorkout(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.workout_data = {
            'title': 'Test workout',
            'user': self.user,
        }
        self.workout = Workout.objects.create(**self.workout_data)

    def test_get_valid_workout(self):
        request = RequestFactory().get('/workouts/')
        serializer_context = {'request': request}
        serializer = WorkoutSerializer(instance=self.workout, context=serializer_context)
        response = self.client.get(reverse('workout-detail', kwargs={'pk': self.workout.pk}))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_workout(self):
        request = RequestFactory().get('/workouts/')
        serializer_context = {'request': request}
        response = self.client.get(reverse('workout-detail', kwargs={'pk': 100}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

