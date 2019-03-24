"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app_skeleton import views
from django.contrib.auth import views as auth_views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    #####################################################
    #                                                   #
    #   Django Admin etc..
    #                                                   #
    #####################################################
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    url(r'^accounts/logout/', auth_views.LogoutView.as_view(template_name = 'registration/logged_out.html'),name='logout'),
    #####################################################
    #                                                   #
    #   App_skeletion urls
    #                                                   #
    #####################################################
    url(r'^$', views.first_page , name='first_page'),
    url(r'^second_page/', views.second_page , name='second_page'),
    url(r'^download_cleaned_file/', views.download_cleaned_file , name='download_cleaned_file'),

    ]
