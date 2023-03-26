from django.urls import path
from .views import workouts, HomeView



urlpatterns = [
    path('workouts/', workouts, name='workout_list'),
    path('', HomeView.as_view(), name='homeView')
]
