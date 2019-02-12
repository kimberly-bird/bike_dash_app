from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class BikeModel(SafeDeleteModel):
    """Bike Model Model (Each bike brand has multiple bike models that are manufactured by that brand)
    
    Arguments:
        SafeDeleteModel -- safe delete policy for all foreign keys
    
    Returns:
        Bike Model instance
    """

    _safedelete_policy = SOFT_DELETE_CASCADE

    brand = models.ForeignKey("Brand", on_delete=_safedelete_policy)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
