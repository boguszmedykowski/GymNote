from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

app_name='note'

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet)
router.register(r'exercise', ExerciseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]