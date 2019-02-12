from django.contrib.auth.models import User
from django import forms

from bikes.models import Brand
from bikes.models import BikeModel
from bikes.models import Bike
from bikes.models import Labor
from bikes.models import Part


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'location',)


class BikeModelForm(forms.ModelForm):
    class Meta:
        model = BikeModel
        fields = ('name',)

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ('brand', 'bikemodel', 'condition', 'name', 'year', 'description', 'purchase_price', 'purchase_date', 'document',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bikemodel'].queryset = BikeModel.objects.none()
    
        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['bikemodel'].queryset = BikeModel.objects.filter(brand_id=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty bike model queryset
        elif self.instance.pk:
            self.fields['bikemodel'].queryset = self.instance.brand.bikemodel_set.order_by('name')


class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ('notes', 'time', 'rate_of_pay', 'bike')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # only put bikes that are not sold in the drop down when adding labor
        bikes_not_sold = Bike.objects.exclude(status=1)
        self.fields['bike'].queryset = bikes_not_sold


class PartForm(forms.ModelForm):

    part_make = forms.CharField(required=False)
    part_model = forms.CharField(required=False)

    class Meta:
        model = Part
        fields = ('bike', 'brand', 'bikemodel', 'parttype', 'name', 'part_make', 'part_model', 'notes', 'purchase_price', 'document',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['bikemodel'].queryset = BikeModel.objects.none()
        
            if 'brand' in self.data:
                try:
                    brand_id = int(self.data.get('brand'))
                    self.fields['bikemodel'].queryset = BikeModel.objects.filter(brand_id=brand_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty bike model queryset
            elif self.instance.pk:
                self.fields['bikemodel'].queryset = self.instance.brand.bikemodel_set.order_by('name')
        
        # user cannot select bike model on dropdown unless they go back to the form after selecting brand
        except AttributeError as err:
            print("error", err)


        self.fields['bike'].required = False
        self.fields['brand'].required = False
        self.fields['bikemodel'].required = False

    

                    
