from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=88)
    released = models.DateTimeField(blank=True, null=True)
    file_type = models.CharField(max_length=44, blank=True)
    path = models.CharField(max_length=250, unique=True)
    duration = models.CharField(max_length=88)
