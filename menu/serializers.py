from rest_framework import serializers
from sales.serializers import SaleSerializer

class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.ImageField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

class ItemSaleSerializers(serializers.Serializer):
    item = ItemSerializer()
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=7, decimal_places=2)
    sale = SaleSerializer()