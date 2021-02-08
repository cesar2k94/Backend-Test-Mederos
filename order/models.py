from django.db import models

# Create your models here.
class order(models.Model):
    option=models.IntegerField()
    specify=models.CharField(max_length=100)
    user_id=models.IntegerField(auto_created=1)
    created=models.DateField(auto_now_add=True)
    username=models.CharField(max_length=40, default="name")

    def __str__(self):
        return self.specify

