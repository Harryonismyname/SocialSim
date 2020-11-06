from re import error
from django.db import models
from ..login.models import User
# Create your models here.

class CharacterManager(models.Manager):
    def character_validator(self, postData):
        errors = {}
        if len(postData['first_name'])<1:
            errors['noName'] = 'Please enter a name'
        return errors

class Character(models.Model):
    objects = CharacterManager()
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characters')
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255, default='')
    bio= models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class ConnectionManager(models.Manager):
    def connection_validator(self, postData):
        errors={}
        if postData['who'] == postData['to_whom']:
            errors['selfConnect'] = 'You cannot create a relationship between someone and themselves'
        selectedCharacter = Character.objects.get(id=postData['who'])
        targetedCharacter = Character.objects.get(id=postData['to_whom'])
        if selectedCharacter.connections.filter(contact=targetedCharacter):
            errors['doubleConnect'] = f'{selectedCharacter.first_name} {selectedCharacter.last_name} already has a connection with {targetedCharacter.first_name} {targetedCharacter.last_name}'
        return errors

class Connections(models.Model):
    objects = ConnectionManager()
    owner = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="connections")
    contact = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='contact_id')
    opinion = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Log(models.Model):
    connection = models.ForeignKey(Connections, on_delete=models.CASCADE, related_name='log')
    actor = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='actions')
    action = models.CharField(max_length=255)
    recipient = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='recieved_actions')
    result = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)