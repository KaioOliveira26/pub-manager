from django.db import models
from sales.models import Sale


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='items/')
    price = models.DecimalField(max_digits=10, decimal_places=2)


class ItemSale(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
