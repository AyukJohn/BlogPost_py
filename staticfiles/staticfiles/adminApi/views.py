# from django.shortcuts import render

# # Create your views here.
# from ..api_basic.models import Articles
# from .models import Articles
# from ..api_basic.serializers import ArticleSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework import request, status
# from rest_framework.views import APIView
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User as user



# # Create your views here.

# ### class based views

# class AdminApi(APIView):

#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request):
#         articles = Articles.objects.filter()
#         serializer = ArticleSerializer(articles, many = True,context= {'request': request})
#         # count = articles.count()
#         return Response( { 'tasks':serializer.data })
#         # return Response({
#         #     'tasks':(len(articles), serializer.data)
#         # })
#         return Response(serializer.data)


#     # permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save(user=request.user)
#             # user = serializer.save()
            
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)






# class AdminArticleDetailApi(APIView):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    

#     def get_object(self, pk):
#         try:
#             return Articles.objects.get(id = pk)
    
#         except Articles.DoesNotExist:
#             return Response(status= status.HTTP_404_NOT_FOUND)



#     def get(self,request,pk):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article, context= {'request': request})
#         return Response( { 'tasks':serializer.data })



#     def put(self, request,pk):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article,data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.save(user = request.user)
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



#     def delete(self, request, pk):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

