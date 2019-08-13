from django.urls import path
from user import views

urlpatterns = [
    path('', views.userpostlist, name='userpostlist'),
    path('newpost/',views.newpost,name='newpost'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('<slug:slug>/edit/', views.PostEdit.as_view(), name='post_edit'),

    path('image/upload/', views.ImageUploader, name='imageupoload'),
]