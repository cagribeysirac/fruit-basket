from django.db import models
from django.conf import settings


class Fruit(models.Model):
    class FruitType(models.IntegerChoices):
        MEYVE = 0
        SEBZE = 1
        YESILLIK = 2

    name = models.CharField(unique=True, blank=False, null=False, max_length=20)
    type = models.SmallIntegerField(choices=FruitType.choices)
    stock = models.BooleanField()
    min_available = models.IntegerField()
    max_available = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # TODO: ADD IMAGE (may be recordable image path)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.ForeignKey(
        to="fruit.Fruit",
        to_field="name",
        on_delete=models.RESTRICT,
        blank=False,
        null=False,
        related_name="customer",
        db_column="name",
    )
    amount = models.IntegerField()  ## TODO: must be in range min~max available
    state = models.BooleanField()

    def __str__(self):
        return f"{self.customer} | {self.amount} | {self.name}"
