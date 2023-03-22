from rest_framework import routers, serializers, viewsets
from .models import *

class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'