from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # is going to be used when the user is not authenticated
    # serializer.ImageField check doc
    class Meta:
        model = Product
        fields = ["sku", "name", "description", "unit_price", "category"]
        # extra_kwargs docs
        extra_kwargs = {
            "unit_price": {
                "required": True,
            }
        }
        # making validations in serializers

    # def validate_unit_price(self, value):
    #     if value < 10:
    #         raise serializers.ValidationError("hey minimum is 10")
    #     elif value > 1000000:
    #         raise serializers.ValidationError("hey maximum is 10000000")
    #     return value


class FullProductSerializer(serializers.ModelSerializer):
    # is going to be used when the user is authenticated
    class Meta:
        model = Product
        fields = "__all__"
