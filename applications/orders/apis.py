from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from applications.orders.serializers import (
    ReadOrderSerializer,
    ReadOrderItemSerializer,
    WriteOrderSerializer
)
from applications.orders.models import Order, OrderItem


class OrderView(APIView):
    serializer_class = ReadOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        ser = self.serializer_class(orders, many=True)
        return Response(ser.data)

    def post(self, request):
        model_object = WriteOrderSerializer(
            data=request.data
        )  # change the serializer later
        if model_object.is_valid():  # will call validate_items
            model_object.save()  # we want to write logic for what happens when we call the save function
            return Response(model_object.data, status=201)
        return Response(model_object.errors, status=500)


class OrderItemView(APIView):
    serializer_class = ReadOrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_items = OrderItem.objects.all()
        ser = self.serializer_class(my_items, many=True)
        return Response(ser.data)


class OrderDetailView(APIView):
    serializer_class = ReadOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_order(self, pk):
        try:
            return Order.objects.get(id=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_order(pk)
        ser = self.serializer_class(order)
        return Response(ser.data)
