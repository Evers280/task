from django.shortcuts import render
from rest_framework import viewsets
from .models import Tasks, Masters
from .serializers import TasksSerializer, MastersSerializer



# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
class MastersViewSet(viewsets.ModelViewSet):
    queryset = Masters.objects.all()
    serializer_class = MastersSerializer
    