# django restframework
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import EngPermission

from applications.country.models import Country
from applications.country.serializers import CountrySerializer

# function based views and class based views


country_data: list = [
    {
        "short_name": "DE",
        "full_name": "Germany",
        "capital": "Berlin",
        "president": "",
        "population": 29000000,
        "currency": "EUR",
        "no_of_states": 20,
    },
    {
        "short_name": "NIG",
        "full_name": "Nigeria",
        "capital": "Lagos",
        "president": "",
        "population": 36000000,
        "currency": "NAR",
        "no_of_states": 36,
    },
]


# fucntion based views
# @api_view(["GET", "POST"])
# def list_countries(request):
#     # what do you wanna do with that request
#     # dont forget to give a response

#     # ideally data will come from your models
#     # status.HTTP_200_OK

#     # what should happen when the request is a get
#     if request.method == "GET":
#         my_ser = CountrySerializer(country_data, many=True)
#         return Response(my_ser.data)
#     elif request.method == "POST":
#         print(request.data)
#         country_data.append(request.data)
#         return Response(country_data)


# @api_view(["GET", "PUT", "DELETE"])
# def country_detail(request, pk):
#     # use the pk to find or look for the country
#     # then do something with the country
#     # model.objects.get(id=pk)
#     try:
#         country = country_data[pk]
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         return Response(country)
#     elif request.method == "PUT":
#         country_data[pk] = request.data
#         return Response(country_data[pk])


# class based views


class CountryList(APIView):
    # django specific var
    # authentication_classes = [
    #     TokenAuthentication
    # ]
    # by default you have said, every is permitted to view you country list
    # django specific var
    permission_classes = [IsAuthenticated]

    # django specific methodname
    def get(self, request, *args):
        countries = Country.objects.all()  # we have some countries here ()
        # these countries are python objects
        # solution is to convert that complex python object to a transmittable data type( JSON, XML)
        extract_country_info = CountrySerializer(countries, many=True)
        return Response(extract_country_info.data)

    # django specific methodname
    def post(self, request, *args):
        # when someone makes a post request (they want to send data to be stored/checked in your db)
        # -- 1 you want to validate and check that the data is in the right format
        # second thing is use the data
        # return a response
        # request.data(JSON) holds data from post request

        python_object = CountrySerializer(data=request.data)  # this is deserialization
        # deserialization is converting data from json to a python object
        if python_object.is_valid():
            python_object.save()  # models# create method of serializers
            # status 201 means you successfully created something
            # status 500 means something went wrong
            return Response(python_object.data, status=201)
        else:
            return Response(python_object.errors, status=500)


class CountryDetail(APIView):
    def fetch_object(self, pk):
        try:
            return country_data[pk]
        except:
            raise Http404

    def get(self, request, pk):
        country = self.fetch_object(pk)
        return Response(country)

    def put(self, request, pk):
        self.fetch_object(pk)
        country_data[pk] = request.data
        return Response(country_data[pk])
