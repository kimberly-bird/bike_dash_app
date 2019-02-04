from django.contrib.auth.models import User
from django import forms

from bikes.models import Brand
from bikes.models import BikeModel
from bikes.models import Bike
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
        fields = ('brand', 'bikemodel', 'condition', 'status', 'name', 'year', 'description', 'purchase_price', 'purchase_date',)
    
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

class PartForm(forms.ModelForm):

    part_make = forms.CharField(required=False)
    part_model = forms.CharField(required=False)

    class Meta:
        model = Part
        fields = ('bike', 'brand', 'bikemodel', 'parttype', 'name', 'part_make', 'part_model', 'notes', 'purchase_price',)
    
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


        self.fields['bike'].required = False
        self.fields['brand'].required = False
        self.fields['bikemodel'].required = False

    

                    
