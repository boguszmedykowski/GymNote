from django.shortcuts import render
import requests
import json

url = 'http://0.0.0.0:8888/'

def workouts(request):
    response = requests.get(f"{url}api/workout/")
    data = response.json()
    return render(request, 'workout/workouts.html', {'data': data})



