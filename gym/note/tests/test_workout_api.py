from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient



from ..models import Workout

from ..serializers import (
    WorkoutSerializer,
    WorkoutDetailSerializer,
)
from django.contrib.auth import get_user_model


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


    def test_create_workout(self):
        """Test creating a workout."""
        payload = {
            'title': 'Sample workout',
            'description': 'Sample description',
            'link': 'http://example.com/workout.pdf',
        }
        res = self.client.post(NOTE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        workout = Workout.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(workout, k), v)
            self.assertEqual(workout.user, self.user)


    def test_partial_update(self):
        """Test partial update of a workout."""
        original_link = 'https://example.com/workout.pdf'
        workout = create_workout(
            user=self.user,
            title='Sample workout title',
            link=original_link,
        )
        payload = {'title': 'New workout title'}
        url = detail_url(workout.id)
        res = self.client.patch(url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        workout.refresh_from_db()
        self.assertEqual(workout.title, payload['title'])
        self.assertEqual(workout.link, original_link)
        self.assertEqual(workout.user, self.user)


    def test_full_update(self):
        """Test full update of workout."""
        workout = create_workout(
            user=self.user,
            title='Sample workout title',
            link='https://exmaple.com/workout.pdf',
            description='Sample workout description.',
        )
        payload = {
            'title': 'New workout title',
            'link': 'https://example.com/new-workout.pdf',
            'description': 'New workout description',
        }
        url = detail_url(workout.id)
        res = self.client.put(url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        workout.refresh_from_db()
        for k, v in payload.items():
            self.assertEqual(getattr(workout, k), v)
        self.assertEqual(workout.user, self.user)


    # def test_update_user_returns_error(self):
    #     """Test changing the workout user results in an error."""
    #     new_user = create_user(email='user2@example.com', password='test123')
    #     workout = create_workout(user=self.user)
    #     payload = {'user': new_user.id}
    #     url = detail_url(workout.id)
    #     self.client.patch(url, payload)
    #     workout.refresh_from_db()
    #     self.assertEqual(workout.user, self.user)


    def test_delete_workout(self):
        """Test deleting a workout successful."""
        workout = create_workout(user=self.user)
        url = detail_url(workout.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Workout.objects.filter(id=workout.id).exists())

    # def test_workout_other_users_workout_error(self):
    #     """Test trying to delete another users workout gives error."""
    #     new_user = create_user(email='user2@example.com', password='test123')
    #     workout = create_workout(user=new_user)
    #     url = detail_url(workout.id)
    #     res = self.client.delete(url)
    #     self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
    #     self.assertTrue(workout.objects.filter(id=workout.id).exists())


