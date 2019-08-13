from django.urls import path
from auth.views import Login,signup ,Logout

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout,name='logout'),
    path('signup/',signup,name='signup')

]