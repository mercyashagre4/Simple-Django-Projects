from django.urls import path
from .views import *

# here we have four end points to get, post, put and delete.
urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('create/', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view()),
]
