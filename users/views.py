from django.contrib.auth.models import User

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

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
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        response.set_cookie(
            'refresh', str(refresh),
            httponly=True,
            path='/token/refresh/',
            samesite='Lax',
            secure=True
        )
        response.set_cookie(
            'access',
            str(refresh.access_token),
            httponly=True,
            path='/',
            samesite='Lax',
            secure=True
        )
        return response


class LoginTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = RefreshToken.for_user(request.user)
        
        response.set_cookie(
            'refresh', str(refresh),
             httponly=True,
             path='/token/refresh/',
             samesite='Lax',
             secure=True
        )
        response.set_cookie(
            'access',
             str(refresh.access_token),
             httponly=True,
             path='/',
             samesite='Lax',
             secure=True
        )
        
        return response


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        response = super().post(request)
        response.delete_cookie('refresh', path='/token/refresh/')
        response.delete_cookie('access', path='/')
        return response