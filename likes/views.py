from rest_framework import generics, permissions
from drf.permissions import IsCreatorOrReadOnly  
from likes.models import Like
from likes.serializers import LikeSerializer



# Create your views here.

class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(creator=profile)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsCreatorOrReadOnly]  
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
