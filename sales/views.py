from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

import json

from .models import Sale
from menu.models import ItemSale,Item
from table.models import Table

from .serializers import SaleSerializer
from user.serializers import UserSerializer
from menu.serializers import ItemSaleSerializers

class SaleView(APIView):
    def post(self, request):
        sale = json.loads(dict(request.data)['data'][0])
        employee = getattr(Token.objects.get(key=sale['user_token']), 'user')
        table = Table.objects.get(id=sale['table_id'])

        saleObject = Sale.objects.create(
            **{"table": table, "total_price": sale['total_price'],'employee':employee})
        
        SaleItems = [ItemSale.objects.create(
            **{
                "item": Item.objects.get(id=item['id']), "quantity":item['quantity'], 
                "total_price":item['total_price'], "sale":saleObject, 
            }) for item in sale['items']]
        
        sale_data = SaleSerializer(saleObject).data
        return Response(sale_data)
