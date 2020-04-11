from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profile_api import serializer
from profile_api import models
from profile_api import permissions

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

class HelloViewSet(viewsets.ViewSet):
    """ Test API viewsets"""
    serializer_class = serializer.HelloSerializer
    def list(self, request):
        """ Return a hello message"""
        a_viewset = [
            'Uses actions (list, retrive, update, partial_update)',
            'Automaticaly maps to a URLs using Routers',
            'Provide more functionality with less code'
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello message"""
        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'HTTP method': 'GET'})

    def update(self, request, pk=None):
        """ Update an object by its ID"""
        return Response({'HTTP method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ handling partial update of an obect"""
        return Response({'HTTP method': 'PATCH'})

    def destroy(self, request, pk=None) :
        """Handle removing an object"""
        return Response({'HTTP method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes =(permissions.UpdateOwnProfile,)
