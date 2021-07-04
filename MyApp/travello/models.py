from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
# class Destination():
#     name : str
#     img : str
#     desc : str
#     price : int
#     offer : bool
    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)  
        
class FacultData(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    Designation = models.TextField(default='NA')
    Dept = models.TextField(default='NA')
    chairman = models.BooleanField(default=False)
    #dateofjoining = models.TextField(default='2010-10-01')
    qual = models.TextField(default='NA')
    email = models.EmailField(default='NA')
    ResInt = models.TextField(default='NA')
    Experience=models.TextField(default='NA')
    CurRes=models.TextField(default='NA')
    CCurTeach=models.TextField(default='NA')
    CourTaught=models.TextField(default='NA')
    Pub = models.TextField(default='NA')
    ProfMem=models.TextField(default='NA')
    senior = models.IntegerField()
    