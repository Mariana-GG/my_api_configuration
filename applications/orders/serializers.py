from rest_framework import serializers
from .models import Order, OrderItem
from applications.products.models import Product
from applications.products.serializers import FullProductSerializer
from applications.accounts.serializers import UserDisplaySerializer


class ReadOrderItemSerializer(serializers.ModelSerializer):
    product = FullProductSerializer()  # its own serializer

    class Meta:
        model = OrderItem
        fields = "__all__"


class ReadOrderSerializer(serializers.ModelSerializer):
    items = ReadOrderItemSerializer(many=True)  # one order many items
    customer = UserDisplaySerializer()  # its own serializer

    class Meta:
        model = Order
        fields = ["id", "items", "customer", "status"]


class WriteOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        # extra_kwargs
        extra_kwargs = {
            "quantity": {"required": True}
        }  # making sure its required, because it a non strict (default) field


class WriteOrderSerializer(serializers.ModelSerializer):
    items = WriteOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "items",
            "customer",
        ]
        extra_kwargs = {
            "customer": {"required": True},
            "items": {"required": True},
        }

    # validation
    # add a validation, such that items cannot be empty
    def validate_items(self, items_value):
        if not items_value:  # []
            raise serializers.ValidationError("items cannot be an empty list")
        return items_value

    def create(self, validated_data: dict):  # django thing
        # gives you access to all the data that has been checked or validated
        pass
        # 1. we want to get the list of all items you sent from post
        order_items: list = validated_data.pop("items")
        created_items_in_db: list = []
        total: float = 0
        # 2. we want to create the order item in the data base
        for _item in order_items:
            try:
                order_item = OrderItem.objects.create(**_item)
                product = Product.objects.get(id=order_item.product.id)
                total += order_item.total
                # 3. we want to update the product quantity
                self.update_product(product, order_item.quantity)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Cant Find Product")
            except Exception as error:
                raise serializers.ValidationError(error)
            else:
                created_items_in_db.append(order_item)

        # 4. we want to connect all the items to a specific order
        order = Order.objects.create(total=total, **validated_data)
        order.items.set(created_items_in_db)  # go back to how to create django models
        return order

    def update_product(self, product: Product, order_item_quantity: int):
        # F Queries research
        new_quantity = product.quantity - order_item_quantity  # hits your database
        if 0 > new_quantity:  # hits your database
            raise serializers.ValidationError("Quantity not available")
        product.quantity = new_quantity
        product.save()  # hits your database
