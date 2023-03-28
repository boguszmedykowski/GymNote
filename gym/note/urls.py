from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'workout', WorkoutViewSet, basename='workout')
router.register(r'exercise', ExerciseViewSet, basename='exercise')

urlpatterns = [
    path('', include(router.urls)),
]
