from django.conf import settings
from django.db import models

"""
Model class of post format.
"""
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.PositiveIntegerField()
    title = models.TextField()
    body = models.TextField()
