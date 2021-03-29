from django.contrib import admin

from menu.models import Item, ItemSale
from sales.models import Sale
from customer.models import Customer
from table.models import Table

admin.site.register([Item,ItemSale, Sale,Customer,Table])