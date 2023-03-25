from django.test import TestCase
from note.models import Workout

from rest_framework import status
from django.test import TestCase, Client
from django.contrib.auth.models import User
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









# class TestGetWorkout(TestCase):

#     def setUp(self):
#         User.objects.create(
#             username='Casperek',
#             email='user5@example.com',
#             password='string')
#         User.objects.create(
#             username='Muffinek',
#             email='user6@example.com',
#             password='$geg54gegdfgf')
#         Workout.objects.create(
#             title='trening1',
#             user= User.objects.get(username='Casperek'))
#         Workout.objects.create(
#             title='trening2',
#             user= User.objects.get(username='Muffinek'))


#     def test_get_workout(self):
#         workout_casper = Workout.objects.get(title='trening1')
#         workout_muffin = Workout.objects.get(title='trening2')
#         self.assertEqual(
#             workout_casper.title, "trening1")
#         self.assertEqual(
#             workout_muffin.title, "trening2")


# client = Client()

# class TestGetAllWorkouts(TestCase):

#     def setUp(self):
#         Workout.objects.create(
#             title='Casper',)
#         Workout.objects.create(
#             title='Muffin')

#     def test_get_all_workout(self):

#         response = client.get('/api/workout/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


#     def test_get_one_workout(self):

#         response = client.get('/api/workout/2/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)