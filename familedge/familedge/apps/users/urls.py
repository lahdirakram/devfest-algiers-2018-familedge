from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    re_path(r'^connect/', views.connect,name="connect"),
    re_path(r'^deconnect/', views.deconnect,name="deconnect"),

]