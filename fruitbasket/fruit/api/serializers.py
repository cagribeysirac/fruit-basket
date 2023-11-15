from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from fruit.models import Fruit, Item


class FruitSerializer(serializers.Serializer):
    FruitType = (("0", "MEYVE"), ("1", "SEBZE"), ("2", "YESILLIK"))

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=20, validators=[UniqueValidator(queryset=Fruit.objects.all())]
    )
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

    def validate_min_available(self, value):  # Field level validation
        if value < 0:
            raise serializers.ValidationError(
                "Lütfen kabul edilebilecek minimum sipariş miktarını pozitif tam sayı giriniz."
            )
        return value


class ItemSerializer(serializers.Serializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.StringRelatedField()
    amount = serializers.IntegerField()
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

    def validate(self, data):  # Object level validation
        fruit = Fruit.objects.get(name=data["name"])
        if data["amount"] < fruit.min_available or data["amount"] > fruit.max_available:
            raise serializers.ValidationError(
                f"{fruit.name} ürününden {data['amount']} miktarında sipariş edilemez. Sipariş miktarı {fruit.min_available}~{fruit.max_available} aralığında olmalıdır."
            )
        return data
