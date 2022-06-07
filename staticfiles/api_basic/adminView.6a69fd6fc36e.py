from .models import Articles
from .serializers import CommentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as user
from .models import Comment
from api_basic import serializers



class ArticleComment():
    
    def comment(self, request):
        comments = Comment.objects.filter()

        serializer = CommentSerializer(comments, many = True,)
        d = (serializer.data)

        # return ArticleComment.comment
        return (d)

