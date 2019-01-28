from django.db import models
from django.db.models import *


class Part(models.Model):
    bike = models.ForeignKey(
        "Bike",
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
    )
    bikemodel = models.ForeignKey(
        "BikeModel",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    notes = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
