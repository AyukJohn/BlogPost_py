from django.urls import path,include
from .views import *
from knox import views as knox_views
# from .import views

urlpatterns = [
    # path('list/', views.list, name='list'),
    path('v1/api/auth',include('knox.urls')),
    path('v1/api/auth/login', LoginAPI.as_view(), name='login'),
    path('v1/api/auth/register', RegisterAPI.as_view()),
    path('v1/api/auth/user', UserAPI.as_view()),
    path('v1/api/auth/logout', knox_views.LogoutView.as_view(), name='logout')
    # path('article_detail/<str:pk>', views.ArticleDetailApi.as_view()),
]