from django.db import models
import datetime
from django.core.validators import MinValueValidator

# Create your models here.

class menu(models.Model):
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    date=models.DateField(validators=[MinValueValidator(limit_value=datetime.date.today)])
    