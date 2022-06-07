from rest_framework.serializers import Serializer
from .models import Articles,Comment
from .serializers import ArticleSerializer,CommentSerializer
# from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import request, status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User as user
# from .adminView import ArticleComment
from api_basic import serializers
# from .models import Comment


# Create your views here.

### class based views

class AdminApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        articles = Articles.objects.filter()
        serializer = ArticleSerializer(articles, many = True,context= {'request': request})
        return Response( { 'tasks':serializer.data })

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(user=request.user)
            
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




class adminArticleDetailApi(APIView):
    permission_classes = [IsAuthenticated]
    

    def get_object(self, pk):
        try:
            return Articles.objects.get(id = pk)
    
        except Articles.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)



    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, context= {'request': request})
        return Response( { 'tasks':serializer.data })


    def put(self, request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article,data=request.data)
        
        if serializer.is_valid():
            user = serializer.save(user = request.user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




class userArticleApi(APIView):
    
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many = True,context= {'request': request})

        # count = articles.count()
        return Response( { 'tasks':serializer.data })




class userArticleDetailApi(APIView):
    def get_object(self, pk):
        try:
            return Articles.objects.get(id = pk)
    
        except Articles.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, context= {'request': request})
        return Response( { 'tasks':serializer.data })



class CommentsApi(APIView):
    
    def get(self, request):
        comments = Comment.objects.all()

        serializer = CommentSerializer(comments, many = True,)
        context = (serializer.data)

        return Response(context)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)




class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(id = pk)
    
        except Comment.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)

    def get(self,request,pk):
        article = self.get_object(pk)
        serializer = CommentSerializer(article)
        return Response( serializer.data )






## function based api views

# @api_view(["POST", "GET"])
# # @permission_classes([IsAuthenticated])
# def article_list(request):
#     if request.method == 'GET':

#         articles = Articles.objects.all()
#         serializer = ArticleSerializer(articles,  many = True, context= {'request': request} )
#         return Response( { 'tasks':serializer.data })

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