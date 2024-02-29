from django.db.models import Count
from rest_framework import generics,filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf.permissions import IsCreatorOrReadOnly

from .models import Post
from .serializers import PostSerializer


# Create your views here.


class PostList(generics.ListCreateAPIView):
    
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['creator__followed__creator__profile', 'likes__creator__profile', 'creator__profile']
    search_fields = ['creator__username', 'title']
    ordering_fields = ['likes_count', 'comments_count', 'likes__created_at']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.profile)
    def post(self, request, *args, **kwargs):
        print("POST request received for PostList view")
        print("Request user:", request.user)
        print("Request data:", request.data)
        return super().post(request, *args, **kwargs)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    
    permission_classes = [IsCreatorOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    
    def post(self, request, *args, **kwargs):
        print("POST request received for PostDetail view")
        print("Request user:", request.user)
        print("Request data:", request.data)
        return super().post(request, *args, **kwargs)
    