from django.db import models
import re
from datetime import date

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['Username'])<2:
            errors['Username'] = "Username must be greater than 2 characters long"
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address"
        all_users = User.objects.all()
        for user in all_users:
            if user.email == postData['email']:
                errors['unique_email'] = "That email address is already in use"
        if len(postData['password'])<8:
            errors['password'] = "Password must contain at least 8 characters"
        if postData['password'] != postData['conf_pw']:
            errors['conf_pw'] = "Passwords must match"
        return errors

class User(models.Model):
    objects = UserManager()
    username = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password= models.CharField(max_length=45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)