from rest_framework.views import APIView
from rest_framework.response import Response 

class HelloApiView(APIView):
    """ Test Api view """
    def get(self, request, format=None):
        """Returns a list of api view featurs"""
        an_apiview = [
            'Uses HTTP method as afunctions (get, post, patch, put, delete)',
            'Is samilar to traditional django view',
            'Gives you the more control over logic',
            'Is mapped manualy to the URLs',
        ]
        return Response({'massage': 'Hello!', 'an_apiview': an_apiview})
