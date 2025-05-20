from django.db import models

# Create your models here.
class Tasks(models.Model):
    
    STATUS_CHOICES = [
        ('à faire', 'À faire'),
        ('en cours', 'En cours'),
        ('terminé', 'Terminé'),
    ]
    
    titre = models.CharField(max_length=200)
    description = models.TextField()
    priorite = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateField()
    status = models.CharField(max_length=20, default='Á faire')
    
    masters = models.ForeignKey('Masters', on_delete=models.CASCADE, related_name='tasks')
    
    def __str__(self):
        return self.titre
    
class Masters(models.Model):
    
    SEXE_CHOICES = [
        ('masculin', 'Masculin'),
        ('femminin', 'Feminin'),
    ]
    
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    sexe = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nom