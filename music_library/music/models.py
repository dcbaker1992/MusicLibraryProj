from django.db import models


# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    artist = models.CharField(max_length=50, blank=True, null=True)
    album = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
