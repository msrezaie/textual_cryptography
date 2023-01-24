from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    full_name = models.CharField(max_length=200, null= True, blank=True)
    email = models.EmailField(max_length=200, null= True, blank=True)
    long_bio = models.TextField(null= True, blank=True)
    short_bio = models.CharField(max_length=200, null= True, blank=True)
    location = models.CharField(max_length=200, null= True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, default="no-image.jpg")
    profile_background = models.ImageField(null=True, blank=True, default="no-image.jpg")
    social_github = models.CharField(max_length=200, null= True, blank=True)
    social_linkedin = models.CharField(max_length=200, null= True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.full_name)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null= True, blank=True)
    name = models.CharField(max_length=200, null= True, blank=True)
    description = models.TextField(null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)


class Project(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="no-image.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
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
