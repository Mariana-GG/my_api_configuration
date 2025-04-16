from django.db import models
from decimal import Decimal
from .enums import StatusChoices
from applications.fields import decimal_fields

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="orders",  # always have this
    )  # user.orders
    total = models.DecimalField(**decimal_fields)
    status = models.CharField(
        max_length=30,
        choices=StatusChoices.choices(),
        default=StatusChoices.default(),
    )
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="items",
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="items",
        blank=True,  # explain this later
        null=True,
    )
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(
        **decimal_fields
    )  # we will want to automatically calculate the total of product unit_price * quantity

    def __str__(self):
        return f"Item {self.id} for order {self.order}"

    def save(self, *args, **kwargs):
        total = self.quantity * float(self.product.unit_price) # convert decimal to float
        self.total = total
        super().save(*args, **kwargs)
