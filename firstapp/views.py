from django.shortcuts import render
from .models import Todos
from .serializers import TodosSerializer
from rest_framework import viewsets

class TodosViewSet(viewsets.ModelViewSet):
    queryset =  Todos.objects.all()
    serializer_class = TodosSerializer
    
# Create your views here.
