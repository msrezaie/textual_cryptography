import os
from django.contrib.auth.models import User
from django.db import models

class CryptodenUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user
    
class Page(models.Model):
    background = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return os.path.basename(self.background.name)

class Operation(models.Model):
    name = models.CharField(max_length=200)
    cipher = models.ManyToManyField('Cipher')
    desc = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.name

class Cipher(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.name