from rest_framework import serializers
from .models import *

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'link', 'created_by', 'created_at', 'description']
        read_only_fields = ['id']



class WorkoutDetailSerializer(WorkoutSerializer):
    class Meta(WorkoutSerializer.Meta):
        fields = WorkoutSerializer.Meta.fields + ['description']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'