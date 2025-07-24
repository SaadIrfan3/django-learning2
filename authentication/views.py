#from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework import status, permissions

from .models import Players
from .serializers import PlayerSerializer

class RegisterPlayerView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        #if User.objects.filter(username=username).exists():
           # return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        #refresh = RefreshToken.for_user(user)

        return Response({
           "message": "User registered successfully",
           #"refresh": str(refresh),
           #"access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class PlayerAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        players = Players.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
#class UserListView(generics.ListAPIView):
        #queryset = User.objects.all()
       # serializer_class = PlayerSerializer
       # permission_classes = [IsAdminUser]