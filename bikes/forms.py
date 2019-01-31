from django.contrib.auth.models import User
from django import forms

from bikes.models import Brand
from bikes.models import BikeModel


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
