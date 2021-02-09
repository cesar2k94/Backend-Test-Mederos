from django.db import models
import datetime,uuid
from django.core.validators import MinValueValidator

# Create your models here.

class menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    date=models.DateField(validators=[MinValueValidator(limit_value=datetime.date.today)])
    