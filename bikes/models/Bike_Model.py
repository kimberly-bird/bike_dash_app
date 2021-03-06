from django.contrib.auth.models import User
from django.db import models
from django.db.models import *

from .Labor_Model import Labor
from .Part_Model import Part

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
    purchase_date = models.DateField(blank=True, null=True)
    list_price = models.PositiveIntegerField(null=True)
    sale_price = models.PositiveIntegerField(null=True)
    sale_date = models.DateField(blank=True, null=True)
    document = models.FileField(upload_to='documents/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def current_user(self):  
        return self.request.user
    
    @property
    def total_profit(self):
        '''this method calculates the total labor recorded on a sold bike to be used in the bike dashboard to be deducted from the total bike sales
        
        Returns:
            integer -- total $ of labor per bike
        '''
        if self.status.name == "Sold":
            all_labor = Labor.objects.filter(bike_id=self.id)
            total_labor = 0
            for labor in all_labor:
                # call property method on labor model that multiplies rate of pay * time
                labor_calculation = labor.total_for_each_labor
                total_labor += labor_calculation
            return total_labor

    @property
    def part_total_on_bike(self):
        '''This method is to get all of the parts on a bike and calculate their total purchase price sum

        Returns:
            intger -- total $ of parts per bike
        '''
        all_parts = Part.objects.filter(bike_id=self.id)
        total_part_investment = 0
        for part in all_parts:
            total_part_investment += part.purchase_price
        return total_part_investment





