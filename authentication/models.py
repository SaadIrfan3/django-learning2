
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User


class Players(models.Model):
    
    def __str__(self):
        return self.user.username

