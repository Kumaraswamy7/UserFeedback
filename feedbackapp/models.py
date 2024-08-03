from django.db import models

# Create your models here.


class UserData(models.Model):
    usrname =models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=100)
    feedback = models.TextField(max_length=100)
    suggestion = models.TextField(max_length=100)

class UsrFeed(models.Model):
    feedback = models.TextField(max_length=100)
    suggestion = models.TextField(max_length=100)
