from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class ToDo(SafeDeleteModel):
    """ToDo Model
    
    Arguments:
        SafeDeleteModel -- safe delete policy for all foreign keys
    
    Returns:
        ToDo instance
    """
    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.ForeignKey(User, on_delete=_safedelete_policy)
    title = models.CharField(max_length=55)
    notes = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    @property
    def total_todo_labor(self):
        """Property method that calculates the total amount of labor investment per to do item
        
        Returns:
            int -- $ amount
        """
        total_labor = 0
        # loop over labor set and calculate total time/rate of pay
        for todo in self.labor_set.all():
            # total_for_each_labor is a property method on the Labor model that multiplies rate*time
            total_labor += todo.total_for_each_labor
        return total_labor
    

