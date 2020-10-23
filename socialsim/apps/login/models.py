from django.db import models
import re
from datetime import date

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name'])<2:
            errors['first_name'] = "First name must be greater than 2 characters long"
        if len(postData['last_name'])<2:
            errors['last_name'] = "Last name must be greater than 2 characters long"
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address"
        all_users = User.objects.all()
        for user in all_users:
            if user.email == postData['email']:
                errors['unique_email'] = "That email address is already in use"
        if postData['bdate'] > str(date.today()):
            errors['bdate'] = "Please enter a valid date"
        limit_date = date.today().year-13
        restricted_day = date.today()
        age_limit_date = date.replace(restricted_day,year=limit_date)
        if postData['bdate'] >str(age_limit_date):
            errors['age'] = "You must be 13 years old to register"
        if len(postData['password'])<8:
            errors['password'] = "Password must contain at least 8 characters"
        if postData['password'] != postData['conf_pw']:
            errors['conf_pw'] = "Passwords must match"
        return errors

class User(models.Model):
    objects = UserManager()
    first_name = models.CharField(max_length=45)
    last_name= models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    bdate= models.DateField()
    password= models.CharField(max_length=45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)