from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class Labor(SafeDeleteModel):
    """Labor Model
    
    Arguments:
        SafeDeleteModel -- safe delete policy for all foreign keys
    
    Returns:
        Labor instance
    """
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
        """method that calculates the total amount of labor in dollars based off of time and rate of pay
        
        Returns:
            int -- calculated time*rate of pay
        """

        return self.time * self.rate_of_pay

