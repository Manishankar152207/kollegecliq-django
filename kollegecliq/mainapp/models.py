from email import message
from django.db import models

# Create your models here.
class RegisteredUsers(models.Model):
    user_id = models.CharField(primary_key=True,max_length=55)
    username = models.CharField(max_length=55,default=0)
    name = models.CharField(max_length=55,null=True)
    email = models.CharField(max_length=55)
    phone = models.CharField(max_length=14)
    password = models.CharField(max_length=260)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now=True)
    is_live = models.CharField(max_length=2,default='0')

class Contact(models.Model):
    name = models.CharField(max_length=55,null=False)
    email = models.CharField(max_length=55)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    
    