from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Workout
from .serializers import WorkoutSerializer

from django.shortcuts import render
import requests
class WorkoutViewSet(viewsets.ModelViewSet):

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    # @action(detail=True, methods=['get'])
    # def my_view(self, request, pk=None):
    #     workout = self.get_object()
    #     serializer = self.get_serializer(workout)
    #     url = reverse('workout-my_view', kwargs={'pk': pk})
    #     return Response({'workout': serializer.data, 'url': url})

