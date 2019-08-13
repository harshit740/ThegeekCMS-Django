"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from CMS import settings

urlpatterns = [
    path('auth/',include('auth.urls')),
    path('me/',include('user.urls'),),
    path('',include('blog.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.SITE_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL + "public/", document_root=settings.MEDIA_ROOT + "public/")

