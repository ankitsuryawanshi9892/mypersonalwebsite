from django.contrib import admin
from django.urls import path
from . import views
from .views import contactus

urlpatterns = [
    path("", views.about, name= "Home"),
    path("contactus/", views.contactus, name= "Contact"),
    path("about/", views.about, name= "About"),
    path("project/", views.project, name= "Projects"),
]
