from django.test import TestCase
from note.models import Workout

from rest_framework import status
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        workout = Workout.objects.create(
            created_by=user,
            title='Sample workout name',
            description='Sample workout description.',
        )

        self.assertEqual(str(workout), workout.title)