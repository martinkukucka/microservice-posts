from django.conf import settings
from django.db import models


class Post(models.Model):
    """
    Model class of post format.
    """
    id = models.AutoField(primary_key=True)
    userId = models.PositiveIntegerField()
    title = models.TextField()
    body = models.TextField()
