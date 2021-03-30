# from django.shortcuts import render, redirect
# from django.template.response import TemplateResponse
# from django.contrib.contenttypes.models import ContentType

# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import Customer

# from .serializers import CustomerSerializer

# class CustomerView(APIView):
#     def post(self,request):
#         customer = dict(request.data)
#         customer = CustomerSerializer(Customer.objects.create(**customer)).data
#         return Response(customer)