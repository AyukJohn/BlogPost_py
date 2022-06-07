from pyexpat import model
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Articles
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    count_assigned = serializers.SerializerMethodField()
   

    class Meta:
        model = Comment
        fields = ['id', 'comments','emailAddress','article','count_assigned']

    def get_count_assigned(self, obj):
        return Comment.objects.count()




class ArticleSerializer(serializers.ModelSerializer):

    count_assigned = serializers.SerializerMethodField()

    # comments = serializers.PrimaryKeyRelatedField(many = True, read_only=True)

    class Meta:
        model = Articles
        fields = ['id', 'title','subtitle','body','count_assigned','date', 'img','comments' ]


    def get_count_assigned(self, obj):
        return Articles.objects.count()
        # fields = '__all__'

    
    def get_comment(self, obj):
        return Comment.objects()
   
   


# class CommentSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Comment
#         fields = ['id', 'comments']
