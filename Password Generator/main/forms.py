from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.core.validators import MinLengthValidator, MaxLengthValidator

class PassGenForm(forms.Form):
    #length = forms.IntegerField(min_value = 6, max_value = 20, localize = True)
    #age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'placeholder': 'Age'}))
    length = forms.IntegerField(min_value = 6,
                                widget=forms.NumberInput(attrs={'placeholder': 'Enter password length ...', 'class':'input-length'}))

    
    