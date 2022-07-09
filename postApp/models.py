from django.conf import settings
from django.db import models


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2048)