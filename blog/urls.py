from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.PostListByCategory.as_view(), name='categry_postlist'),


]
