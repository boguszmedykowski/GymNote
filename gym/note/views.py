from .models import Workout
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import (
    viewsets,
    mixins,
)




class WorkoutViewSet(viewsets.ModelViewSet):

    serializer_class = WorkoutDetailSerializer
    queryset = Workout.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkoutSerializer
        else:
            return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseViewSet(mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """Manage exercises in the database."""
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')
