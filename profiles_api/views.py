from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, filters
from rest_framework import viewsets
from profiles_api import serializers, models, permissions

# Create your views here.
class HelloApiView( APIView ):
  """API VIEW de prueba """
  
  serializer_class = serializers.HelloSerializer

  def get( self, request, format=None ):
    """Retornar listas de caracteristicas del apiview"""
    an_apiview = [
      'Usamos metodos Http como funciones (get, post, patch, put, delete)'
    ]

    return Response({'message':'Hello', 'an_apiview': an_apiview})

  def post( self, request ):
    '''Crea un mensaje con nuestro nombre'''
    serializer = self.serializer_class( data = request.data )
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello { name }'
      return Response({ 'message': message })
    else:
      return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
      )
    
  def put( self, request, pk=None):
    ''' Maneja actualizar un objeto '''
    return Response({ 'method':'PUT' })

  def patch( self, request, pk=None):
    """Maneja actualizacion parcial de un objeto"""
    return Response({ 'method':'PATCH' })

  def delete( self, request, pk=None):
    """Elimina un objeto"""
    return Response({ 'method':'DELETE' })


class HelloViewSet(viewsets.ViewSet):
  """Test Api viewset"""
  serializer_class = serializers.HelloSerializer

  def list( self, request):
    """Retornar mensaje de Hola mundo"""
    an_viewset = [
      'Usa acciones (List,create,retrieve,update,partial_update)',
      'Automaticamente mapea a los urls usando routers',
      'Provee mas funcionalidad con menos codigo'
    ]

    return Response({ 'message':'Hola mundo', 'an_viewset': an_viewset })
  
  def create( self, request ):
    '''Crea un mensaje con nuestro nombre'''
    serializer = self.serializer_class( data = request.data )
    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f'Hello { name }'
      return Response({ 'message': message })
    else:
      return Response(
        serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
      )
  def retrieve(self, request, pk=None):
    #Obtiene un objeto y su ID
    return Response({'http_method': 'GET'})
  
  def update(self, request, pk=None):
    #Actualiza un objeto
    return Response({'http_method': 'PUT'})

  def partial_update(self, request, pk=None):
    #Actualiza parcialmente un objeto
    return Response({'http_method': 'PACTH'})

  def destroy(self, request, pk=None):
    #Elimina parcialmente un objeto
    return Response({'http_method': 'DELETE'})

class UserProfileViewSet( viewsets.ModelViewSet ):
  """Crea y actualiza un objeto"""
  serializer_class = serializers.UserProfileSerializer
  queryset       = models.UserProfile.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (permissions.UpdateOwnProfile,)
  filter_backends   = (filters.SearchFilter,)
