# django restframework
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from applications.accounts.serializers import (
    UserSerializer,
    UserDisplaySerializer,
)
from django.contrib.auth.models import User


class UserRegistrationView(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        model_object = self.serializer_class(data=request.data)
        if model_object.is_valid():
            user = model_object.save()
            Token.objects.get_or_create(user=user)
            return Response({"message": "User created"}, status=201)
        return Response(model_object.errors, status=500)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(
            username=request.data["username"],
            password=request.data["password"],
        )
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                }
            )
        return Response({"error": "Invalid Credentials"}, status=401)


class ListUsersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        ser = UserDisplaySerializer(users, many=True)
        return Response(ser.data)


class UserDetailView(APIView):
    serializer_class = UserDisplaySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_user(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_user(pk)
        ser = self.serializer_class(user)
        return Response(ser.data)

    def put(self, request, pk):
        user = self.get_user(pk)
        ser = self.serializer_class(user, data=request.data)
        return Response(ser.data)
