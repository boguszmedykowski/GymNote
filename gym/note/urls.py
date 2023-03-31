from django.urls import path, include
from rest_framework import routers
from .views import *

app_name='note'

router = routers.DefaultRouter()
router.register(r'workouts', WorkoutViewSet)
router.register(r'exercise', ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]