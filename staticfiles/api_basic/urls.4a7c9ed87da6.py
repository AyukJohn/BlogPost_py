from .import views
from django.urls import path



urlpatterns = [
    # path('v1/api/userArticle', views.article_list),
    # path('v1/api/articleDetails', views.article_details),
    path('v1/api/admin_article', views.AdminApi.as_view()),
    path('v1/api/userArticle', views.userArticleApi.as_view()),
    path('v1/api/ArticleComment', views.CommentsApi.as_view()),
    path('v1/api/commentDetail/<str:pk>', views.CommentDetail.as_view()),
    path('v1/api/adminArticle_detail/<str:pk>', views.adminArticleDetailApi.as_view()),
    path('v1/api/userArticle_detail/<str:pk>', views.userArticleDetailApi.as_view()),
]