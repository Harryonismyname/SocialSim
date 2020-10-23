from django.urls import path
from . import views

urlpatterns = [
    path('title', views.index),
    path('create/character', views.create_character),
    path('create/connection', views.add_contact)
]