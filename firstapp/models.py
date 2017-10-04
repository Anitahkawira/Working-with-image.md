from django.db import models

# Create your models here.
class Post(models.Model):
    userId = models.IntegerField(default=1)
    id = models.AutoField("id", primary_key=True)
    title = models.CharField("Title",max_length = 200)
    completed = models.TextField(default="false")
    

