from rest_framework import serializers
from .models import *




class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']




class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for workouts."""
    exercises = ExerciseSerializer(many=True, required=False)

    class Meta:
        model = Workout
        fields = [
            'id', 'title', 'link',
            'exercises',
        ]
        read_only_fields = ['id']


    def _get_or_create_exercises(self, exercises, workout):
        """Handle getting or creating exercises as needed."""
        auth_user = self.context['request'].user
        for exercise in exercises:
            exercise_obj, created = Exercise.objects.get_or_create(
                user=auth_user,
                **exercise,
            )
            workout.exercises.add(exercise_obj)

    def create(self, validated_data):
        """Create a workout."""
        exercises = validated_data.pop('exercises', [])
        workout = Workout.objects.create(**validated_data)
        self._get_or_create_exercises(exercises, workout)

        return workout

    def update(self, instance, validated_data):
        """Update workout."""
        exercises = validated_data.pop('exercises', None)
        if exercises is not None:
            instance.exercises.clear()
            self._get_or_create_exercises(exercises, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance









class WorkoutDetailSerializer(WorkoutSerializer):
    class Meta(WorkoutSerializer.Meta):
        fields = WorkoutSerializer.Meta.fields + ['description']
        read_only_fields = WorkoutSerializer.Meta.read_only_fields


