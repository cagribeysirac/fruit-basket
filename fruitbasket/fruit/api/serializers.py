from rest_framework import serializers
from fruit.models import Fruit


class FruitSerializer(serializers.Serializer):
    class FruitType(serializers.ChoiceField):
        MEYVE = 0
        SEBZE = 1
        YESILLIK = 2

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(unique=True, blank=False, null=False, max_length=20)
    type = serializers.IntegerField(choices=FruitType.choices)
    stock = serializers.BooleanField()
    min_available = serializers.IntegerField()
    max_available = serializers.IntegerField()
    creation_time = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Fruit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.type = validated_data.get("type", instance.type)
        instance.stock = validated_data.get("stock", instance.stock)
        instance.min_available = validated_data.get(
            "min_available", instance.min_available
        )
        instance.max_available = validated_data.get(
            "max_available", instance.max_available
        )
        instance.save()

        return instance
