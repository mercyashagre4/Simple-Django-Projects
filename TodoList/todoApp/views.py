from django.shortcuts import render
from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# because of IsAuthenticatedOrReadOnly, if there is any one who hasn't been authebticated, they wiil be allowed to read only but won't be allowed to put delete and create

# Create your views here.

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

