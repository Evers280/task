from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated # Importer la permission IsAuthenticated
from .models import Tasks, Masters
from .serializers import TasksSerializer, MastersSerializer



# Create your views here.
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]  # Assurez-vous que l'utilisateur est authentifié
    
    def get_queryset(self):
        # Ne montre que les tâches de la personne connectée
        return Tasks.objects.filter(masters=self.request.masters)

    def perform_create(self, serializer):
        # Quand on crée une tâche, on met automatiquement la personne connectée
        serializer.save(masters=self.request.master)
    
class MastersViewSet(viewsets.ModelViewSet):
    queryset = Masters.objects.all() # Récupérer tous les masters
    serializer_class = MastersSerializer # permet de convertir les données en JSON
    permission_classes = [IsAuthenticated]  # Assurez-vous que l'utilisateur est authentifié
    
    def get_queryset(self):
        # Seuls les admins peuvent voir tous les utilisateurs, sinon on limite
        if self.request.user.is_superuser: # si l'utilisateur est admin
            return Masters.objects.all()
        else:
            return Masters.objects.filter(id=self.request.masters.id) # Limiter aux masters connectée
        