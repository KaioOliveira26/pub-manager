from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length =50 )
    cpf = models.CharField(max_length =12, unique=True )
    phone = models.CharField(max_length = 12 )