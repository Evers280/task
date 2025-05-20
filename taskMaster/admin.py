from django.contrib import admin
from .models import Tasks, Masters

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'priorite', 'date_creation', 'date_echeance', 'status')
    search_fields = ('titre', 'description')
    list_filter = ('status', 'priorite')

class MastersAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'sexe', 'email')
    search_fields = ('nom', 'prenom')
    list_filter = ('sexe',)
    
admin.site.register(Tasks, TasksAdmin)   
admin.site.register(Masters, MastersAdmin)