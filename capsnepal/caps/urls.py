from django.contrib import admin
from django.urls import path, include
from caps import views
from caps.views import about


urlpatterns = [
    path("",views.index, name='home'),
    path("home",views.index, name='home'),
    path("about",views.about, name='about'),
    path("login",views.login, name='login'),
    path("register",views.register, name='register'),
    path("show_create_caps",views.show_create_caps, name='show_create_caps'),
    path("create_caps",views.create_caps, name='create_caps'),
    path("show_caps",views.show_caps, name='show_caps')
]