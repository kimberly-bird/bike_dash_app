from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Labor(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    notes = models.CharField(max_length=55)
    date = models.DateField(auto_now=False, auto_now_add=True)
    time = models.PositiveIntegerField()
    rate_of_pay = models.PositiveIntegerField()
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}'
