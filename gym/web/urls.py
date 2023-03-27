from django.urls import path
from .views import (workouts,
                    registration,
                    Home)



urlpatterns = [
    path('workouts/', workouts, name='workout_list'),
    path('', Home, name='homepage'),
    path('registration/', registration, name='registration'),
    path('login/', registration, name='login'),
]
