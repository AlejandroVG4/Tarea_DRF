from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import InputSerializer, OutputSerializer
from .models import Usuarios
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

def index(request):
    titulo = 'Aplicación para usuarios'
    return render(request, 'index.html', {
        'titulo': titulo
    })
    
class SignUp(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if Usuarios.objects.filter(email=serializer.validated_data['email']).exists():
            return Response("Email already registered", status=status.HTTP_400_BAD_REQUEST)
        
        if Usuarios.objects.filter(username=serializer.validated_data['username']).exists():
            return Response("Username already registered", status=status.HTTP_400_BAD_REQUEST)
        
        user = Usuarios.objects.create_user(**serializer.validated_data)
        
        refresh = RefreshToken.for_user(user)
        
        serializer = OutputSerializer({
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "pais": user.pais,
            "direccion": user.direccion,
            "telefono": user.telefono,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        })
        
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)