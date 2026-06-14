from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.Modelserializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed', 'created_at']
        read_only_filds = ['created_at']