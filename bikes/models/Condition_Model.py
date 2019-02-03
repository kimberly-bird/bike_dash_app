from django.db import models
from django.db.models import *

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_NOCASCADE


class Condition(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_NOCASCADE
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
