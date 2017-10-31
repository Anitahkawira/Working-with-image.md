from django.db import models

# Create your models here.
class Todos(models.Model):
    userId = models.IntegerField(default=1)
    title = models.CharField("Title",max_length = 200)
    body = models.TextField(default="Body of post goes here")
    picture = models.ImageField(default="default.png")
