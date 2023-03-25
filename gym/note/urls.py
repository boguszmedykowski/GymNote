from django.urls import path, include
from rest_framework import routers
from .views import WorkoutViewSet

router = routers.DefaultRouter()
router.register(r'workout', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', include(router.urls)),
]
