"""netflix16ocak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appMy.views import *
from appUser.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('netflix/<id>/', netflixPage, name='netflixPage'),
    # USER 
    path('profile/', profilePage, name='profilePage'),
    path('account/', accountPage, name='accountPage'),
    path('login/', loginUser, name='loginUser'),
    path('logout/', logoutUser, name='logoutUser'),
    path('register/', registerUser, name='registerUser'), 
    path('profildelete/<id>/', profilDelete, name='profilDelete'),
    path('filmler/', film_listesi, name='film_listesi'),
    path('diziler/', dizi_listesi, name='dizi_listesi'),
    path('film-ekle/', film_ekle, name='film-ekle'),
    path('dizi-ekle/', dizi_ekle, name='dizi-ekle'),
     path('filmler/<int:pk>/', film_detay, name='film_detay'),
    path('diziler/<int:pk>/', dizi_detay, name='dizi_detay'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
