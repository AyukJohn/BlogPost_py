
from .models import TutorialModel
from .serializers import TaskSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User as userfrom django.shortcuts import render

# Create your views here.



class TutorialApi(APIView):
    def get(self, request):
        articles = TutorialModel.objects.filter()
        serializer = TaskSerializers(articles, many = True,)
        return Response(serializer.data)


    

    def post(self, request):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            # user = serializer.save(user=request.user)
            user = serializer.save()
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
