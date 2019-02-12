from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Labor(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.ForeignKey(User, on_delete=_safedelete_policy)
    notes = models.CharField(max_length=55)
    date = models.DateField(auto_now=False, auto_now_add=True)
    time = models.PositiveIntegerField()
    rate_of_pay = models.PositiveIntegerField()
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}'

    @property
    def get_total_for_each_labor(self):
        return self.time * self.rate_of_pay

    @property
    def get_total_labor(self):
        labor = Labor.objects.filter(pk=self.id)

        for l in labor:
            total_labor += l.time * l.rate_of_pay 
        return total_labor
