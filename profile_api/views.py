from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializer

class HelloApiView(APIView):
    """ Test Api view """
    serializer_class = serializer.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of api view featurs"""
        an_apiview = [
            'Uses HTTP method as afunctions (get, post, patch, put, delete)',
            'Is samilar to traditional django view',
            'Gives you the more control over logic',
            'Is mapped manualy to the URLs',
        ]
        return Response({'massage': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello massage with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'massage': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})            
