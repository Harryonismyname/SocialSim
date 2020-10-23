from django.db import models
from ..login.models import User
# Create your models here.
class Character(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    age= models.IntegerField(default=0)
    title= models.CharField(default='', max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Connections(models.Model):
    owner = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="connections")
    contact = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='contact_id')
    opinion = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)