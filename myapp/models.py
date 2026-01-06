from django.db import models

# Create your models here.

class Item(models.Model):
    item_no = models.CharField(max_length=50)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()