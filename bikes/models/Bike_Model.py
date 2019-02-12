from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Bike(SafeDeleteModel):
    """Bike Model
    
    Arguments:
        SafeDeleteModel -- safe delete policy for all foreign keys
    
    Returns:
        Bike instance
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.ForeignKey(User, on_delete=_safedelete_policy)
    brand = models.ForeignKey("Brand", on_delete=_safedelete_policy)
    bikemodel = models.ForeignKey("BikeModel", on_delete=_safedelete_policy)
    condition = models.ForeignKey("Condition", on_delete=_safedelete_policy)
    status = models.ForeignKey("Status", on_delete=_safedelete_policy)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    description = models.CharField(max_length=255)
    purchase_price = models.PositiveIntegerField()
    purchase_date = models.CharField(max_length=255)
    list_price = models.PositiveIntegerField(null=True)
    sale_price = models.PositiveIntegerField(null=True)
    sale_date = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(upload_to='documents/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'

