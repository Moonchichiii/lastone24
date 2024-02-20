from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CurrentProfileSerializer


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my Last API"
    })
    
    

class CurrentProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CurrentProfileSerializer(request.user)
        return Response(serializer.data)