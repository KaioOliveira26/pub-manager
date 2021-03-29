from rest_framework import serializers
from table.serializers import TableSerializer
from user.serializers import UserSerializer

class SaleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    table = TableSerializer()
    employee = UserSerializer()
    total_price = serializers.DecimalField(max_digits=12, decimal_places=2)
    date = serializers.DateTimeField() 