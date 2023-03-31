from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient



CREATE_USER_URL = reverse('users:create')



def create_user(**params):
    return get_user_model().objects.create_user(**params)



