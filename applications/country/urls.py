from django.urls import path
from applications.country import apis


urlpatterns = [
    path("countries/", apis.CountryList.as_view()),
    path("countries/<int:pk>/", apis.CountryDetail.as_view()),
]
