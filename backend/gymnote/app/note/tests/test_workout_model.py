from django.test import TestCase
from note.models import Workout

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_recipe(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        workout = Workout.objects.create(
            user=user,
            title='Sample workout name',
            description='Sample workout description.',
        )

        self.assertEqual(str(workout), workout.title)