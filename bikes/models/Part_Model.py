from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Part(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.ForeignKey(User, on_delete=_safedelete_policy)
    bike = models.ForeignKey("Bike", on_delete=_safedelete_policy, blank=True, default=None, null=True)
    brand = models.ForeignKey("Brand", on_delete=_safedelete_policy, blank=True, default=None, null=True)
    bikemodel = models.ForeignKey("BikeModel", on_delete=_safedelete_policy, blank=True, default=None, null=True)
    parttype = models.ForeignKey("PartType", on_delete=_safedelete_policy)
    name = models.CharField(max_length=255)
    part_make = models.CharField(max_length=255, blank=True, null=True)
    part_model = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    notes = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()
    document = models.FileField(upload_to='documents/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'
