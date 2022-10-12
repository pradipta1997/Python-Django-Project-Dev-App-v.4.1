from turtle import title
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    # Ini adalah OOP Python untuk merubah nama Post pada admin agar sesuai dengan nama title
    def __str__(self):
        return "{}".format(self.title)
