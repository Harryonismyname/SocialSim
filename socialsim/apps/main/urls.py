from django.urls import path
from . import views

urlpatterns = [
    path('title', views.index),
    path('create/character', views.create_character),
    path('create/connection', views.add_contact),
    path('about/<int:id>', views.about),
    path('edit/<int:id>', views.edit_character),
    path('delete/<int:id>', views.delete),
    path('interact/<int:id>', views.interact),
    path('remove/contact/<int:id>', views.remove_contact)
]