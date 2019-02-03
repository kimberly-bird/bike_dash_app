from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Part(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    bike = models.ForeignKey("Bike",)
    brand = models.ForeignKey("Brand",)
    bikemodel = models.ForeignKey("BikeModel",)
    parttype = models.ForeignKey("PartType",)
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    notes = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
