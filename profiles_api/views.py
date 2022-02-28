from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


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