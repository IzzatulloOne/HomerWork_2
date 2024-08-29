from django import forms
from .models import Brand, Color, Car

class BrandForm(forms.Form):
    name = forms.CharField(max_length=100)

class ColorForm(forms.Form):
    name = forms.CharField(max_length=100)

class CarForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    date_manufacture = forms.DateField()
    count = forms.IntegerField()
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    color = forms.ModelChoiceField(queryset=Color.objects.all())
