from rest_framework import serializers
from fruit.models import Fruit, Item


class FruitSerializer(serializers.Serializer):
    FruitType = (("0", "MEYVE"), ("1", "SEBZE"), ("2", "YESILLIK"))

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    type = serializers.ChoiceField(choices=FruitType)
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


class ItemSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.StringRelatedField()
    amount = serializers.IntegerField()  ## TODO: must be in range min~max available
    ordered = serializers.BooleanField()
    action_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.ordered = validated_data.get("ordered", instance.ordered)
        instance.save()
        return instance
