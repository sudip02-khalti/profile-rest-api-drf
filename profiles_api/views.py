from pyexpat import model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.authentication import TokenAuthentication
from .permissions import *


class TestingView(APIView):
    """Test APIView"""

    def get(self, request):
        return Response({'status': 200, 'message': 'Testign view is completed!'})

    def post(self, request):
        serial_data = ProfileSerializer(data=request.data)
        if serial_data.is_valid():
            name = serial_data.validated_data.get('name')
            message  = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serial_data.errors, stauts=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk=None):
        """Put method to update the details"""

        return Response({'message': 'PUT method'})

    def patch(self, request, pk=None):
        """Patch method to partial update"""

        return Response({'message': 'PATCH method'})

    def delete(self, request, pk=None):
        """DELETE method to delte details"""
        return Response({'messge': 'DETETE method'})

    
class viewsetclass(viewsets.ViewSet):
    """viewsets api """

    def list(self, request):
        return Response({'message': 'This is the viewset list method'})

    
    def create(self, requet):
        serializer = ProfileSerializer(data=requet.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return f'Hello {name}'
        
        else:
            return Response(serializer.errors, stauts=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        """Retive teh single element from  the details"""

        return Response({'message': 'PUT method'})

    def update(self, request, pk=None):
        """Update method to partial update"""

        return Response({'message': 'PATCH method'})
    
    def partial_update(self, request, pk=None):
        """Patch method to partial update"""

        return Response({'message': 'PATCH method'})

    def destroy(self, request, pk=None):
        """destroy method to delte details"""
        return Response({'messge': 'DETETE method'})



class UserProfileViewsets(viewsets.ModelViewSet):
    """Handling and creating and update user profile for individual user"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserloginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles create update and reading profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (
        UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )


    def perform_create(self, serializer):
        """set the user profile to the loggedin user"""
        serializer.save(user_profile=self.request.user)