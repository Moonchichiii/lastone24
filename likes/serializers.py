from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'creator' and 'post'
    """
    creator = serializers.ReadOnlyField(source='creator.username')  

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'creator', 'post'] 

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            }) 