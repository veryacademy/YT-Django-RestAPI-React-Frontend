from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
