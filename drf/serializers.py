from django.contrib.auth.models import User
from rest_framework import serializers

class CurrentProfileSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta:
        model = User
        fields = ('id', 'username','profile_id', 'profile_image')