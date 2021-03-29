from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    cpf = serializers.CharField()
    telefone = serializers.CharField()