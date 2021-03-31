# from django.shortcuts import render, redirect
# from django.template.response import TemplateResponse
# from django.contrib.contenttypes.models import ContentType

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from datetime import datetime

# import json
# import itertools

# from sales.models import Sale
# from menu.models import Item, ItemSale

# from menu.serializers import ItemSerializer, ItemSaleSerializers
# from sales.serializers import SaleSerializer


# class AverageSalesView(APIView):
#     def get(self, request):
#         sales = SaleSerializer(Sale.objects.all(), many=True).data
#         total_sales = len(sales)
#         total_billing = sum([float(sale['total_price']) for sale in sales])
#         average_sale = total_billing/total_sales
#         return Response(average_sale)


# class BestSellingsView(APIView):
#     def get(self, request):
#         items = [{'id': item['item']['id'], 'name':item['item']['name'], 'quantity':item['quantity']}
#                  for item in ItemSaleSerializers(ItemSale.objects.all(), many=True).data]

#         reduced_items = []

#         for item in items:
#             if item['id'] not in [item['id'] for item in reduced_items]:
#                 reduced_items.append(item)

#             for item_saved in reduced_items:
#                 if item['id'] == item_saved['id']:
#                     item_saved['quantity'] += item['quantity']
#         items = []
#         for i in range(9):
#             if len(reduced_items) >= 1:
#                 maxquantity = max([item['quantity'] for item in reduced_items])
#                 items.append(reduced_items.pop(reduced_items.index(
#                     [item for item in reduced_items if item['quantity'] == maxquantity][0])))

#         background_colors = [
#             'rgba(54, 162, 235, 0.7)',
#             'rgba(30, 99, 132, 0.7)',
#             'rgba(255, 206, 86, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#         ]
#         data = {'title': 'Produtos mais vendidos', 'values': [item['quantity'] for item in items],
#                 'labels': [item['name'] for item in items], 'backgroundColors': background_colors}

#         return Response(data)


# class LessSoldView(APIView):
#     def get(self, request):
#         items = [{'id': item['item']['id'], 'name':item['item']['name'], 'quantity':item['quantity']}
#                  for item in ItemSaleSerializers(ItemSale.objects.all(), many=True).data]

#         reduced_items = []

#         for item in items:
#             if item['id'] not in [item['id'] for item in reduced_items]:
#                 reduced_items.append(item)

#             for item_saved in reduced_items:
#                 if item['id'] == item_saved['id']:
#                     item_saved['quantity'] += item['quantity']

#         items = []
#         for i in range(9):
#             if len(reduced_items) >= 1:
#                 maxquantity = min([item['quantity'] for item in reduced_items])
#                 items.append(reduced_items.pop(reduced_items.index(
#                     [item for item in reduced_items if item['quantity'] == maxquantity][0])))

#         background_colors = [
#             'rgba(54, 162, 235, 0.7)',
#             'rgba(30, 99, 132, 0.7)',
#             'rgba(255, 206, 86, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#         ]
#         data = {'title': 'Produtos menos vendidos', 'values': [item['quantity'] for item in items],
#                 'labels': [item['name'] for item in items], 'backgroundColors': background_colors}

#         return Response(data)


# class SalesView(APIView):
#     def get(self, request):
#         items = [{'id': item['item']['id'], 'name':item['item']['name'], 'quantity':item['quantity']}
#                  for item in ItemSaleSerializers(ItemSale.objects.all(), many=True).data]
#         week_days = [
#             'Segunda-feira',
#             'Terça-feira',
#             'Quarta-feira',
#             'Quinta-Feira',
#             'Sexta-feira',
#             'Sábado',
#             'Domingo'
#         ]

#         # reduced_items = []

#         # for item in items:
#         #     if item['id'] not in [item['id'] for item in reduced_items]:
#         #         reduced_items.append(item)

#         #     for item_saved in reduced_items:
#         #         if item['id'] == item_saved['id']:
#         #             item_saved['quantity'] += item['quantity']

#         sales = SaleSerializer(Sale.objects.all(), many=True).data
#         item_in_sales = [[{'id': item['item']['id'], 'name':item['item']['name'], 'quantity':item['quantity'], 'date':item['sale']['date']}
#                           for item in ItemSaleSerializers(ItemSale.objects.filter(sale=sale['id']), many=True).data] for sale in sales]

#         items_with_weekday = [[{'id': item['id'],'name': item['name'], 'quantity':item['quantity'], 'weekday':datetime.strptime(
#             item['date'], '%Y-%m-%dT%H:%M:%S.%fZ').weekday()} for item in sale] for sale in item_in_sales]
#         items_with_weekday =list(itertools.chain(*items_with_weekday))
#         weekdays_data = [{'weekday':day,'items':[item for item in items_with_weekday if item['weekday']==key],'sale_quantity':sum([item['quantity'] for item in items_with_weekday if item['weekday']==key])} for key, day in enumerate(week_days)]
        
#         background_colors = [
#             'rgba(54, 162, 235, 0.7)',
#             'rgba(30, 99, 132, 0.7)',
#             'rgba(255, 206, 86, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#             'rgba(200, 0, 192, 0.7)',
#         ]

#         data = {'title':'vendas na semana','values': [week_day['sale_quantity'] for week_day in weekdays_data],
#                 'labels': [week_day['weekday'] for week_day in weekdays_data], 'backgroundColors': background_colors}

#         return Response(data)


# class DashBoardView(APIView):
#     def get(self, request):
#         return render(request, "dashboard.html")
