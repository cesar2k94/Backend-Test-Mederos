from django import forms 
from .models import order

class OrderForm(forms.ModelForm):
    class Meta:
        model=order
        fields=['option','specify']
        widgets={
            'option': forms.NumberInput( attrs = { 'step' : 1 , 'max' : 4 , 'min' : 1 }),
            'specify': forms.Textarea(),
            
        }