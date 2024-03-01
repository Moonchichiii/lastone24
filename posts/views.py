from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf.permissions import IsCreatorOrReadOnly

from .models import Post
from .serializers import PostSerializer


# Create your views here.


class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [IsCreatorOrReadOnly]

    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter,
                       filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['creator__creator__username']


    search_fields = ['title', 'ingredients', 'recipe', 'time']
    ordering_fields = ['likes_count', 'comments_count', 'likes__created_at']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.profile)

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
