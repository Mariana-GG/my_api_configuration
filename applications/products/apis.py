from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
)
from rest_framework.authentication import (
    TokenAuthentication,
    BasicAuthentication,
)
from applications.products.serializers import (
    ProductSerializer,
    FullProductSerializer,
)
from applications.products.models import Product


class ProductView(APIView):
    # is been used for documentations purposes
    serializer_class = ProductSerializer  # django specific
    authentication_classes = [TokenAuthentication, BasicAuthentication] # how you can choose to authenticate yourself
    # permission_classes = [IsAuthenticated] # you must

    def get_permissions(self):  # django specific
        api_method: str = self.request.method
        if api_method == "POST":
            return [IsAdminUser()]
        else:
            return [AllowAny()]

    def get(self, request):
        all_products = Product.objects.all()
        my_serializer = self.serializer_class(
            all_products, many=True
        )  # its already holding a json object
        return Response(my_serializer.data)

    def post(self, request):
        # deserialize data
        model_object = ProductSerializer(data=request.data)
        if model_object.is_valid():  # false
            model_object.save()
            return Response(model_object.data, status=201)
        return Response(model_object.errors, status=500)


class ProductDetailView(APIView):
    serializer_class = FullProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_my_product(self, pk):  # not django specific
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_my_product(pk)  # can never be more than one product
        my_ser = self.serializer_class(product)
        return Response(my_ser.data)
