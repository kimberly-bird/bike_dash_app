from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Bike(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.ForeignKey(User)
    brand = models.ForeignKey("Brand")
    bikemodel = models.ForeignKey("BikeModel")
    condition = models.ForeignKey("Condition")
    status = models.ForeignKey("Status")
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    description = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()
    purchase_date = models.CharField(max_length=255)
    list_price = models.PositiveIntegerField(null=True)
    sale_price = models.PositiveIntegerField(null=True)
    sale_date = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'{self.name}'

