from django.urls import path
from auth.views import Login,signup

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('signup/',signup,name='signup')
]