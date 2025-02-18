from django.shortcuts import render
from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# I have defined IsAuthenticatedOrReadOnly project level permission in settings.py in line 134
# because of IsAuthenticatedOrReadOnly permission, if there is any one who hasn't been authenticated, they wiil be allowed to read only but won't be allowed to put delete and create

# Create my views

# read
class ListTodo(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# update
class DetailTodo(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

# create
class CreateTodo(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
# delete
class DeleteTodo(generics.DestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

