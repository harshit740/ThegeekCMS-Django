from django.shortcuts import render
from profiles.models import Profile
from django.shortcuts import get_object_or_404 ,redirect ,render
from django.contrib.auth import get_user_model


def getProfile(request,username):
    user =get_user_model()
    user = user.objects.get(username=username)
    print(user)
   # profile = Profile.objects.get(user=user)
    return  render(request,'profile/profile.html',{'profile':user})