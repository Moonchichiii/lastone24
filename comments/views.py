from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf.permissions import IsCreatorOrReadOnly  
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Create your views here.

class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(creator=profile)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you are the creator.
    """
    permission_classes = [IsCreatorOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()