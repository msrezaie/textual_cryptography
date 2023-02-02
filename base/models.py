from django.db import models
from django.contrib.auth.models import User
import uuid
import os

class Page(models.Model):
    landing_page_background = models.ImageField(upload_to='images/', null=True, blank=True)
    logo = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return os.path.basename(self.landing_page_background.name)


class Profile(models.Model):
    full_name = models.CharField(max_length=200, null= True, blank=True)
    email = models.EmailField(max_length=200, null= True, blank=True)
    long_bio = models.TextField(null= True, blank=True)
    short_bio = models.CharField(max_length=200, null= True, blank=True)
    line1 = models.CharField(max_length=200, null= True, blank=True)
    line2 = models.CharField(max_length=200, null= True, blank=True)
    line3 = models.CharField(max_length=200, null= True, blank=True)
    location = models.CharField(max_length=200, null= True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True, default="no-image.jpg")
    profile_background = models.ImageField(upload_to='images/', null=True, blank=True, default="no-image.jpg")
    social_github = models.CharField(max_length=200, null= True, blank=True)
    social_linkedin = models.CharField(max_length=200, null= True, blank=True)
    resume = models.FileField(upload_to='documents/', null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.full_name)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null= True, blank=True)
    STACK_CHOICES = [
        ('front-end', 'Front-end'),
        ('back-end', 'Back-end'),
    ]
    stack = models.CharField(choices=STACK_CHOICES, max_length=20, blank=True)
    skill = models.CharField(max_length=200, null= True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.skill)


class Project(models.Model):
    title = models.CharField(max_length=200)
    long_description = models.TextField(null=True, blank=True)
    short_description = models.TextField(max_length=200, null=True, blank=True)
    featured_image = models.ImageField(upload_to='images/',
        null=True, blank=True, default="no-image.jpg")
    demo_link = models.CharField(default="None", max_length=2000, null=True, blank=True)
    source_link = models.CharField(default="None", max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # unique attribute meaning: no other value can have
    # the same value as the value of the following 'id'
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    class Meta:
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(null= True, blank=True)
    
    def __str__(self):
        return self.name
