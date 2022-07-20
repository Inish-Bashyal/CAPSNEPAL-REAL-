from django.contrib import admin
from django.urls import path, include
from caps import views
from caps.views import about


urlpatterns = [
    path("",views.index, name='Home'),
    path("home",views.about, name='index'),
    path("login",views.login, name='login')
]