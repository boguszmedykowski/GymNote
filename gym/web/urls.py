from django.urls import path
from .views import workouts



urlpatterns = [
    path('workouts/', workouts, name='workout_list')
]
