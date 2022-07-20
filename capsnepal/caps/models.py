from django.db import models

# Create your models here.
class Cap(models.Model):
    image = models.ImageField(upload_to='caps')
    desc = models.TextField(max_length=500)
    price = models.IntegerField()
    qty_sold = models.IntegerField(default=0)
    
    
from django.contrib import admin

admin.site.register(Cap)