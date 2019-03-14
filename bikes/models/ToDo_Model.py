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

    

