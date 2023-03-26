from django.shortcuts import render
import requests
from django.views.generic import ListView
from note.models import Workout


class HomeView(ListView):
    model = Workout
    template_name = "web/index.html"



url = 'http://0.0.0.0:8888/'

def workouts(request):
    response = requests.get(f"{url}api/workout/")
    data = response.json()
    return render(request, 'workout/workouts.html', {'data': data})



