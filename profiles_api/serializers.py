from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    """Serializer the name field for testing of our api"""
    name = serializers.CharField(max_length=20)