from django.db import models
from django.db.models import *


class Labor(models.Model):
    notes = models.CharField(max_length=55)
    date = models.DateField(auto_now=False, auto_now_add=True)
    time = models.PositiveIntegerField()
    rate_of_pay = models.PositiveIntegerField()
    bike_id = models.ForeignKey(
        'Bike', 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.date}'
