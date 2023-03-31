from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .models import Workout

from .serializers import (
    WorkoutSerializer,
    WorkoutDetailSerializer,
)


NOTE_URL = reverse('note:workout-list')

def detail_url(workout_id):
    """Create and return a workout detail URL."""
    return reverse('note:workout-detail', args=[workout_id])

def create_workout(user, **params):
    defaults = {
        'title': 'Sample workout title',
        'description': 'Sample description',
        'link': 'http://example.com/workout.pdf',
    }
    defaults.update(params)

    workout = Workout.objects.create(user=user, **defaults)
    return workout


class PublicWorkoutAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(NOTE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateWorkoutApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_workout(self):
        create_workout(user=self.user)
        create_workout(user=self.user)

        res = self.client.get(NOTE_URL)

        workout = Workout.objects.all().order_by('-id')
        serializer = WorkoutSerializer(workout, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_workout_list_limited_to_user(self):
        other_user = get_user_model().objects.create_user(
            'other@example.com',
            'password123',
        )
        create_workout(user=other_user)
        create_workout(user=self.user)

        res = self.client.get(NOTE_URL)

        workout = Workout.objects.filter(user=self.user)
        serializer = WorkoutSerializer(workout, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)




    def test_get_workout_detail(self):
        """Test get workout detail."""
        workout = create_workout(user=self.user)

        url = detail_url(workout.id)
        res = self.client.get(url)

        serializer = WorkoutDetailSerializer(workout)
        self.assertEqual(res.data, serializer.data)

