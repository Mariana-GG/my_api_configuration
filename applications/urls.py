from django.urls import path, include

urlpatterns = [
    path("", include("applications.country.urls")),
    path("", include("applications.accounts.urls")),
    path("", include("applications.products.urls")),
    path("", include("applications.orders.urls")),
]
# 127.0.0.1:8000/api/v1/countries/ will work
# 127.0.0.1:8000/countries wont work
