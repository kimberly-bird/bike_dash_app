from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class BikeModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    brand = models.ForeignKey("Brand")
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
