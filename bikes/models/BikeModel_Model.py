from django.db import models
from django.db.models import *


class BikeModel(models.Model):
    brand = models.ForeignKey(
    "Brand",
    on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
