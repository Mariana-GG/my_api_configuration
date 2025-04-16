from django.db import models
from .enums import CategoryChoices
import secrets
from applications.fields import decimal_fields


class Product(models.Model):
    #id = integers
    sku = models.CharField( # another way to identify a product apart from using the id
        max_length=15,
        default="",
        blank=True,
        null=True,
    )  # we want to be able to generate the sku in the background
    name = models.CharField(max_length=50)
    description = models.TextField(
        default="",
        blank=True,
    )
    unit_price = models.DecimalField(
        **decimal_fields
    )
    category = models.CharField(
        max_length=30,
        choices=CategoryChoices.choices(),
        default=CategoryChoices.default(),
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Product {self.name} {self.sku}"

    # overiding the save method.
    def save(self, *args, **kwargs):
        # do something useful (we want to automatically generate a sku)
        if not self.sku:  # if sku is empty, generate one for me
            self.sku = f"PROD_ID-{secrets.token_hex(5)}"
        super().save(*args, **kwargs)
