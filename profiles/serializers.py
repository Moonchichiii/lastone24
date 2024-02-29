from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    is_creator = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.creator

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            user_profile = user.profile
            following = Follower.objects.filter(
                creator=user_profile, followed=obj
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'creator', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_creator', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]
