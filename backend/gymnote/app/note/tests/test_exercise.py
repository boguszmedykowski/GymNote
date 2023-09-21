"""
Tests for the exercises API.
"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from note.models import Exercise

from note.serializers import ExerciseSerializer


EXERCISES_URL = reverse('note:exercise-list')


def detail_url(exercise_id):
    """Create and return an exercise detail URL."""
    return reverse('note:exercise-detail', args=[exercise_id])



def create_user(email='user@example.com', password='testpass123'):
    """Create and return user."""
    return get_user_model().objects.create_user(email=email, password=password)


class PublicExercisesApiTests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required for retrieving exercises."""
        res = self.client.get(EXERCISES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateExercisesApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_exercises(self):
        """Test retrieving a list of ingredients."""
        Exercise.objects.create(user=self.user, name='Kale')
        Exercise.objects.create(user=self.user, name='Vanilla')

        res = self.client.get(EXERCISES_URL)

        exercises = Exercise.objects.all().order_by('-name')
        serializer = ExerciseSerializer(exercises, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_exercises_limited_to_user(self):
        """Test list of exercises is limited to authenticated user."""
        user2 = create_user(email='user2@example.com')
        Exercise.objects.create(user=user2, name='Salt')
        exercise = Exercise.objects.create(user=self.user, name='Pepper')

        res = self.client.get(EXERCISES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], exercise.name)
        self.assertEqual(res.data[0]['id'], exercise.id)

    def test_update_exercise(self):
        """Test updating an exercise."""
        exercise = Exercise.objects.create(user=self.user, name='Cilantro')

        payload = {'name': 'Coriander'}
        url = detail_url(exercise.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        exercise.refresh_from_db()
        self.assertEqual(exercise.name, payload['name'])



    def test_delete_exercise(self):
        """Test deleting an exercise."""
        exercise = Exercise.objects.create(user=self.user, name='Lettuce')

        url = detail_url(exercise.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        exercises = Exercise.objects.filter(user=self.user)
        self.assertFalse(exercises.exists())