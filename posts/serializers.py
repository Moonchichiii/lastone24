from rest_framework import serializers
from posts.models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_creator = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='creator.profile.id')
    profile_image = serializers.ReadOnlyField(source='creator.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.creator

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                creator=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'creator', 'is_creator', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
        ]