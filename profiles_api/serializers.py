from webbrowser import get
from rest_framework import serializers
from . models import *

class ProfileSerializer(serializers.Serializer):
    """Serializer the name field for testing of our api"""
    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers user profile objects"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style':{
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        """Create and rerurn new user"""

        user = UserProfile.objects.create_user(
            email = validated_data.get('email'),
            name = validated_data.get('name'),
            password = validated_data.get('password')

        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializer profile feed item"""
    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile':{
                'read_only': True,
            }
        }