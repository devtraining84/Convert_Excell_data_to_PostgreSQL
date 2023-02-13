from django.db import models

# Create your models here.




class PalukRidersModel(models.Model):
    date = models.DateField(null=True)
    firstname = models.CharField(max_length=32)
    secondname = models.CharField(max_length=32, null=True, blank=True)
    lastname = models.CharField(max_length=32)
    payment = models.BooleanField(default=False)
    region = models.CharField(max_length=1)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    kind = models.CharField(max_length=32)
    shirt = models.CharField(max_length=16)
    road = models.CharField(choices=[('ON','ON'),('OFF','OFF')],max_length=3)
    passenger = models.BooleanField(default=False)
    p_shirt = models.CharField(max_length=16, null=True, default="", blank=True)




class PalukRidersModel2(models.Model):
    date = models.DateField(null=True)
    firstname = models.CharField(max_length=32)
    secondname = models.CharField(max_length=32, null=True)
    lastname = models.CharField(max_length=32)
    payment = models.BooleanField(default=False)
    region = models.CharField(max_length=1)
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    kind = models.CharField(max_length=32)
    shirt = models.CharField(max_length=16)
    road = models.CharField(choices=[('ON','ON'),('OFF','OFF')],max_length=3)
    passenger = models.BooleanField(default=False)
    p_shirt = models.CharField(max_length=16, null=True, default="")


