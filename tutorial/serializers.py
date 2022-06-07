from rest_framework import serializers
from .models import TutorialModel

class TaskSerializers(serializers.ModelSerializer):

   
    class Meta:
        model = TutorialModel
        fields = ['id', 'title','description']


   