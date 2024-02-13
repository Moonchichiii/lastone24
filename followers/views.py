from rest_framework import generics, permissions
from drf.permissions import IsCreatorOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication



# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e., all instances of a user
    following another user.
    Create a follower, i.e., follow a user if logged in.
    Perform_create: associate the current logged-in user with a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user) 

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower.
    No Update view, as we either follow or unfollow users.
    Destroy a follower, i.e., unfollow someone if you're the creator.
    """
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer