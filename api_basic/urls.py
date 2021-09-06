from .import views
from django.urls import path



urlpatterns = [
    # path('', views.article_list),
    path('', views.ArticleApi.as_view()),
    path('article_detail/<str:pk>', views.ArticleDetailApi.as_view()),
]