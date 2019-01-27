from django.db import models
from django.db.models import *


class Brand(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
