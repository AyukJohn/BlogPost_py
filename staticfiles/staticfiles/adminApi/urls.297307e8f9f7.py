from .import views
from django.urls import path



urlpatterns = [
    path('v1/api/admin_article', views.AdminApi.as_view()),
    # path('v1/api/article', views.ArticleApi.as_view()),
    path('v1/api/adminarticle_detail/<str:pk>', views.AdminArticleDetailApi.as_view()),
]