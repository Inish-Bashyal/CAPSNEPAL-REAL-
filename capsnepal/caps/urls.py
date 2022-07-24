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
    path("create_caps",views.create_caps, name='create_caps'),
    path("show_caps",views.show_caps, name='show_caps'),
    path("most_viewed",views.most_viewed, name='most_viewed'),
    path("best_seller",views.best_seller, name='best_seller'),
    path("latest_arrivals",views.latest_arrivals, name='latest_arrivals'),
    path("custom_caps",views.custom_caps, name='custom_caps'),
    path("cap_details/<id>",views.cap_details, name='cap_details'),
    path("update_cap/<id>",views.update_cap, name='update_cap'),
    path("delete_cap/<id>",views.delete_cap, name='delete_cap'),

]