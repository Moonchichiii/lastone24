from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf.permissions import IsCreatorOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.


class ProfileList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """

    queryset = Profile.objects.annotate(
        posts_count=Count('creator__post', distinct=True),
        followers_count=Count('creator__followed', distinct=True),
        following_count=Count('creator__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'creator__following__followed__profile',
        'creator__followed__creator__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'creator__following__created_at',
        'creator__followed__created_at',
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the creator.
    """
    permission_classes = [IsCreatorOrReadOnly]  
    queryset = Profile.objects.annotate(
        posts_count=Count('creator__post', distinct=True),
        followers_count=Count('creator__followed', distinct=True),
        following_count=Count('creator__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
