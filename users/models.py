from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=55)
    email = models.CharField(max_length=20)
