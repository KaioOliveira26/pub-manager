from django.db import models
from table.models import Table
from django.contrib.auth.models import User


class Sale(models.Model):
    table = models.ForeignKey(Table, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
