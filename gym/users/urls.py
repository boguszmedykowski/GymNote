from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, RegistrationAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/registration/', RegistrationAPIView.as_view(), name="registration")
]