from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status
from core.user.models import User
from core.project.models import Project
from core.Api.models import ClientSerializers, ProjectSerializers
import datetime

class LoginView(APIView):
    def get(self, request, format=None):
        return Response({'detail':'GET Response'})
    
    def post(self, request, format=None):

        try:
            data = request.data
        except ParseError as error:
            return Response(
                'Invalid JSON - {0}'.format(error.detail),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if 'username' not in data or 'password' not in data:
            return Response(
                'Wrong credentials',
                status = status.HTTP_401_UNAUTHORIZED
            )
        
        user = User.objects.get(username=data['username'])
        if not user:
            return Response(
                'No default user, please create one',
                status = status.HTTP_404_NOT_FOUND
            )
        
        # # serializers = User.
        user_json = ClientSerializers('json',User.objects.filter(username=data['username']))
            
        if user_json.is_valid():
            token = Token.objects.get_or_create(user=user)
            return Response({'user':user_json.data,'token': token[0].key})
        
        return Response(user_json.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientHistorial(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,format=None, *args, **kwargs):
        proj = Project.objects.filter(participa__cliente = self.request.user, fechaFin__lt = datetime.now()).order_by('fechaFin')
        serializer = ProjectSerializers(proj, many=True)
        return Response(serializer.data)
    
    def post(self, request,format=None):
        serializer = ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)