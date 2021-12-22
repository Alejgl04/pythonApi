from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response 
# Create your views here.

class HelloApiView( APIView ):
  """API VIEW de prueba """
  
  def get( self, request, format=None ):
    """Retornar listas de caracteristicas del apiview"""
    an_apiview = [
      'Usamos metodos Http como funciones (get, post, patch, put, delete)'
    ]

    return Response({'message':'Hello', 'an_apiview': an_apiview})

