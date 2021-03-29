from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
from django.contrib.contenttypes.models import ContentType

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

import json

from .models import Item
from .serializers import ItemSerializer


class MenuView(APIView):
    def get(self, request):
        items = json.dumps(ItemSerializer(Item.objects.all(),many=True).data)
        return TemplateResponse(request, 'menu.html', {'items':items})

    def post(self, request):
        return Response(request.data)


class InsertItem(APIView):
    def get(self, request):
        return render(request, 'item_form.html')

    def post(self, request):
        item = Item.objects.create(
            **{key: request.data[key] for key in request.data if key !='csrfmiddlewaretoken'})
        new_item = ItemSerializer(item).data
        return redirect('../menu/')
