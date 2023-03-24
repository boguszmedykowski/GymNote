from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer



class RegistrationAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)