from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .models import Profile
from .serializers import ProfileSerializer
from drf.permissions import IsCreatorOrReadOnly  


# Create your views here.


class ProfileList(generics.ListAPIView):    
    permission_classes = [IsAuthenticatedOrReadOnly]
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """    
    queryset = Profile.objects.annotate(
        posts_count=Count('posts', distinct=True),
        followers_count=Count('followers', distinct=True),
        following_count=Count('following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]    
    
    filterset_fields = ['creator__username', 'created_at'] 
    ordering_fields = ['posts_count', 'followers_count', 'following_count', 'created_at']


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the creator.
    """    
    permission_classes = [IsCreatorOrReadOnly]    
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('posts', distinct=True),
        followers_count=Count('followers', distinct=True),
        following_count=Count('following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
