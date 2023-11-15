from rest_framework import serializers
from fruit.models import Fruit, Item

from datetime import datetime
from django.utils.timesince import timesince


class FruitSerializer(serializers.ModelSerializer):
    time_since_create = serializers.SerializerMethodField()

    class Meta:
        model = Fruit
        fields = "__all__"
        read_only_fields = ["id", "creation_time", "update_time"]

    def get_time_since_create(self, object):
        now = datetime.now()
        creation_time = object.creation_time.replace(tzinfo=None)
        time_delta = timesince(creation_time, now)
        return time_delta

    def validate_min_available(self, value):  # Field level validation
        if value < 0:
            raise serializers.ValidationError(
                "Lütfen kabul edilebilecek minimum sipariş miktarını pozitif tam sayı giriniz."
            )
        return value


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["customer", "action_time"]

    def validate(self, data):  # Object level validation
        fruit = Fruit.objects.get(name=data["name"])
        if data["amount"] < fruit.min_available or data["amount"] > fruit.max_available:
            raise serializers.ValidationError(
                f"{fruit.name} ürününden {data['amount']} miktarında sipariş edilemez. Sipariş miktarı {fruit.min_available}~{fruit.max_available} aralığında olmalıdır."
            )
        return data
