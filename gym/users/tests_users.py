# from django.test import TestCase
# from django.urls import reverse
# from .models import User
# from rest_framework import status
# from rest_framework.test import APIClient
# from .serializers import UserSerializer
# from note.models import Workout
# from note.serializers import WorkoutSerializer
# from django.test import Client


# class TestGetOneUserLogged(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password': 'testpass'
#         }
#         self.user = User.objects.create_user(**self.user_data)


#     def test_get_valid_user(self):
#         login = self.client.login(username=self.user_data['username'], password=self.user_data['password'])
#         self.assertTrue(login)
#         response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
#         user = User.objects.get(pk=self.user.pk)
#         serializer = UserSerializer(user)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class TestGetOneUser(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password': 'testpass'
#         }
#         self.user = User.objects.create_user(**self.user_data)

#     def test_get_valid_user(self):
#         response = self.client.get(reverse('user-detail', kwargs={'pk': self.user.pk}))
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_get_invalid_user(self):
#         new_user = User.objects.create_user(username='newuser', email='newuser@example.com', password='newpass')
#         response = self.client.get(reverse('user-detail', kwargs={'pk': new_user.pk + 1}))
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)





# # class TestLoggedInUser(TestCase):
# #     def setUp(self):
# #         self.client = APIClient()
# #         self.user = User.objects.create_user(username='testuser', password='testpass')
# #         self.client.login(username='testuser', password='testpass')
# #         self.workout1 = Workout.objects.create(title='Test workout 1', user=self.user)
# #         self.workout2 = Workout.objects.create(title='Test workout 2', user=self.user)
# #         self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
# #         self.workout3 = Workout.objects.create(title='Other user workout', user=self.other_user)

# #     def test_get_workouts_for_logged_in_user(self):
# #         response = self.client.get(reverse('workout-list'))
# #         workouts = Workout.objects.filter(user=self.user)
# #         serializer = WorkoutSerializer(workouts, many=True, context={'request': response.wsgi_request})
# #         self.assertEqual(response.data, serializer.data)
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)



















# # from django.test import TestCase
# # from users.models import User
# # from rest_framework.authtoken.models import Token
# # from rest_framework.test import APIClient
# # from rest_framework import status
# # from django.test import TestCase, Client




# # class TestUser(TestCase):

# #     def setUp(self):
# #         User.objects.create(
# #             username='Casper',
# #             email='user@example.com',
# #             password='string')
# #         User.objects.create(
# #             username='Muffin',
# #             email='user2@example.com',
# #             password='$geg54gegdfgf')

# #     def test_user(self):
# #         user_casper = User.objects.get(username='Casper')
# #         user_muffin = User.objects.get(username='Muffin')
# #         self.assertEqual(
# #             user_casper.username, "Casper")
# #         self.assertEqual(
# #             user_muffin.username, "Muffin")


# # client = Client()

# # class TestGetAllUsers(TestCase):

# #     def setUp(self):
# #         User.objects.create(
# #             username='Casper',
# #             email='user@example.com',
# #             password='string')
# #         User.objects.create(
# #             username='Muffin',
# #             email='user2@example.com',
# #             password='$geg54gegdfgf')

# #     def test_get_all_workout(self):

# #         response = client.get('/api/users/')
# #         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# #     def test_get_one_workout(self):

# #         response = client.get('/api/users/2/')
# #         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




# # ##################################
# # class TestGetAllUsers_as_admin(TestCase):

# #     def setUp(self):
# #         self.admin = User.objects.create_superuser(
# #             username='admin',
# #             email='admin@example.com',
# #             password='admin123'
# #         )
# #         self.client = APIClient()
# #         self.client.login(username='admin', password='admin123')
# #         User.objects.create(
# #             username='Casper',
# #             email='user@example.com',
# #             password='string')
# #         User.objects.create(
# #             username='Muffin',
# #             email='user2@example.com',
# #             password='$geg54gegdfgf')

# #     def test_get_all_workout(self):
# #         response = self.client.get('/api/users/')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)

# #     def test_get_one_workout(self):
# #         response = self.client.get('/api/users/2/')
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
