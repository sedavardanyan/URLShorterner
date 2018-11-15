from django.db import models
from django.contrib.auth.models import User


class Url(models.Model):
    original = models.URLField()
    shortened = models.CharField(max_length=15)
    visits = models.IntegerField(default=0)
    author = models.ForeignKey(User)

