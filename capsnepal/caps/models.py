from unicodedata import name
from django.db import models

# Create your models here.
class Cap(models.Model):
    name = models.TextField(max_length=50, default='')
    image = models.ImageField(upload_to='savedImages')
    desc = models.TextField(max_length=500)
    price = models.IntegerField()
    qty_sold = models.IntegerField(default=0)
    
    
from django.contrib import admin

admin.site.register(Cap)