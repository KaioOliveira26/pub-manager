from rest_framework import serializers


class TableSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ocupped = serializers.BooleanField()
     