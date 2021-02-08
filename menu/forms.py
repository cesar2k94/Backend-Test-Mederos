from django import forms 
from .models import menu
import datetime
from django.core.validators import MinValueValidator

class MenuForm(forms.ModelForm):
    
    class Meta:
        model=menu
        fields= [
            'option1',
            'option2',
            'option3',
            'option4',
            'date']
        labels ={
            'option1': 'Opción 1',
            'option2': 'Opción 2',
            'option3': 'Opción 3',
            'option4': 'Opción 4',
            'date': 'Fecha de Menú',
        }
        widgets ={
            'option1': forms.TextInput(),
            'option2': forms.TextInput(),
            'option3': forms.TextInput(),
            'option4': forms.TextInput(),
            'date': forms.SelectDateWidget(),
        }

class ModifyForm(forms.Form):
    date=forms.DateField(validators=[MinValueValidator(limit_value=datetime.date.today)], widget=forms.SelectDateWidget())