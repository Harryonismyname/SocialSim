from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create_user),
    path('login', views.login),
    path('login/post', views.loginPost),
    path('logout', views.logout)
]  