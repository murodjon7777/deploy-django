from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
# Create your views here.
from .models import Person
from .serializers import TodoSerializer

class ListTodo(ListAPIView):
    queryset=Person.objects.all()
    serializer_class=TodoSerializer
    
class DetailTodo(RetrieveAPIView):
    queryset=Person.objects.all()
    serializer_class=TodoSerializer
