from rest_framework import serializers
from .models import ToDo

# importing serializers and serialize the objects into suitable format(json) to be utilized by any language and platform
class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')
        
        
        
