from django.db import models

class Table(models.Model):
    ocupped = models.BooleanField(default=False)