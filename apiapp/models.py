from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField(max_length=55)
    massages=models.CharField(max_length=55)
