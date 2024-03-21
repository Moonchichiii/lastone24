from django.contrib.auth import get_user_model
from rest_framework import serializers

class CurrentProfileSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')    
    last_login = serializers.ReadOnlyField() 
    
    

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_id', 'profile_image', 'last_login')
        
        
        
    