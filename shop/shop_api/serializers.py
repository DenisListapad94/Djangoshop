from rest_framework import serializers
from catalog.models import Clothes


class ClothesSerializer(serializers.Serializer):
    name = serializers.CharField()
    size = serializers.IntegerField()
    price = serializers.FloatField()

    def create(self, validated_data):
        return Clothes.objects.create(**validated_data)


class ClothesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ['id', 'name', 'size', 'price']
