from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    creator = serializers.ReadOnlyField(source='creator.username')  
    is_creator = serializers.SerializerMethodField()  
    profile_id = serializers.ReadOnlyField(source='creator.profile.id')  
    profile_image = serializers.ReadOnlyField(source='creator.profile.image.url')  
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_creator(self, obj):  
        request = self.context['request']
        return request.user == obj.creator  

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'creator', 'is_creator', 'profile_id', 'profile_image',  
            'post', 'created_at', 'updated_at', 'content'
        ]

class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read-only field so that we don't have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
