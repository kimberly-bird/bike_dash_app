from django.contrib.auth.models import User
from django.db import models
from django.db.models import *


class Bike(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.CASCADE,
    )
    bikemodel = models.ForeignKey(
        "BikeModel",
        on_delete=models.CASCADE,
    )
    condition = models.ForeignKey(
        "Condition",
        on_delete=models.CASCADE,
    )
    status = models.ForeignKey(
        "Status",
        on_delete=models.CASCADE,
    )
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    description = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()
    purchase_date = models.CharField(max_length=255)
    list_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    sale_date = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

