from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer

# Create your views here.


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        response = Response(status=status.HTTP_201_CREATED)
        response.set_cookie('refresh', str(refresh), httponly=True,
                    path='/token/refresh/', samesite='None', secure=True, max_age=3600 * 24 * 14)
        response.set_cookie('access', str(refresh.access_token),
                    httponly=True, path='/', samesite='None', secure=True, max_age=3600 * 24 * 14)
        return response


class LoginTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = RefreshToken.for_user(request.user)
        response.set_cookie('refresh', str(refresh), httponly=True,
                    path='/token/refresh/', samesite='None', secure=True, max_age=3600 * 24 * 14)
        response.set_cookie('access', str(refresh.access_token),
                    httponly=True, path='/', samesite='None', secure=True, max_age=3600 * 24 * 14)

        return response


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = JsonResponse(
            {"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        response.delete_cookie('refresh', path='/token/refresh/')
        response.delete_cookie('access', path='/')
        return response
