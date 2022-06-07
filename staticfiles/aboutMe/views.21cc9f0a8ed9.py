from warnings import filters
from django.http import response
from django.shortcuts import render

from accounts import serializers
from .models import AboutMe
from .serializers import AboutMeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AboutMeApi(APIView):

    def get(self, request):
        about = AboutMe.objects.filter()
        serializer = AboutMeSerializer(about, many = True,context= {'request': request})
        return Response( { 'about':serializer.data })
        # return Response(serializer.data)




    def post(self, request):
        serializer = AboutMeSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # if(serializer.save()):
            #     return Response('hy')


            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)








class AboutDetail(APIView):

    # permission_classes = [IsAuthenticated]
    

    def get_object(self, pk):
        try:
            return AboutMe.objects.get(id = pk)
    
        except AboutMe.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)



    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = AboutMeSerializer(article, context= {'request': request})
        return Response( { 'tasks':serializer.data })



    def put(self, request,pk):
        article = self.get_object(pk)
        serializer = AboutMeSerializer(article,data=request.data)
        
        if serializer.is_valid():
            # user = serializer.save(user = request.user)
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
