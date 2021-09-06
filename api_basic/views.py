from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import request, status
from rest_framework.views import APIView
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

### class based views

class ArticleApi(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ArticleDetailApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    

    def get_object(self, pk):
        try:
            return Article.objects.get(id = pk)
    
        except Article.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)



    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)



    def put(self, request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




### function based api views

# @api_view(["POST", "GET"])

# def article_list(request):
#     if request.method == 'GET':

#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# @api_view(["PUT", "GET", "DELETE"])

# def article_details(request,pk):
#     try:
#          article = Article.objects.get(id = pk)
    
#     except Article.DoesNotExist:
#         return Response(status= status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)


#     elif request.method == "PUT":
#         serializer = ArticleSerializer(article,data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)