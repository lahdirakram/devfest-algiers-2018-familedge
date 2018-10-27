from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    re_path(r'^connect/$', views.connect,name="connect"),
    re_path(r'^deconnect/$', views.deconnect,name="deconnect"),
    re_path(r'^objective/$', views.objective,name="objective"),
    re_path(r'^dashboard/$', views.dashboard,name="dashboard"),
    re_path(r'^hist/$', views.hist,name="hist"),



]