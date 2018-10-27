from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    re_path(r'^home/$', views.home,name="home"),
    re_path(r'^post/$', views.post,name="post"),
    re_path(r'^quiz/$', views.quizView,name="quiz"),


]