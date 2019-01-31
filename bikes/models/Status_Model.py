from django.db import models
from django.db.models import *


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'