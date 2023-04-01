from rest_framework import serializers
from .models import *

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'link', 'user', 'created_at', 'description']
        read_only_fields = ['id']



class WorkoutDetailSerializer(WorkoutSerializer):
    class Meta(WorkoutSerializer.Meta):
        fields = WorkoutSerializer.Meta.fields + ['description']
        read_only_fields = WorkoutSerializer.Meta.read_only_fields


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'