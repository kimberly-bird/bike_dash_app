from django.db import models
from django.db.models import *


class Part(models.Model):
    bike_id = models.ForeignKey(
        "Bike",
        on_delete=models.CASCADE,
    )
    brand_id = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
    )
    bikemodel_id = models.ForeignKey(
        "BikeModel",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    notes = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
