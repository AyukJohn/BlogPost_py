from .import views
from django.urls import path



urlpatterns = [
    # path('v1/api/article', views.article_list),
    # path('v1/api/articleDetails', views.article_details),
    path('v1/api/aboutMe', views.AboutMeApi.as_view()),
    # path('v1/api/About', views.userArticleApi.as_view()),
    path('v1/api/aboutDetail/<str:pk>', views.AboutDetail.as_view()),
    # path('v1/api/userArticle_detail/<str:pk>', views.userArticleDetailApi.as_view()),

]