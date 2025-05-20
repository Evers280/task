from rest_framework import serializers
from .models import Tasks, Masters

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        
    
class MastersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Masters
        fields = '__all__'        