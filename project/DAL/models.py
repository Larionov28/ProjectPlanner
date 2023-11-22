from django.contrib.auth.models import AbstractUser
from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Сделайте поле email уникальным
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title
