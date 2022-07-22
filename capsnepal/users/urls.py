from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path("register_user",views.register_name, name='register_user'),
    path("login_user",views.login_user, name='login_user')
]