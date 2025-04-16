from django.urls import path
from applications.products import apis


urlpatterns = [
    path("products/", apis.ProductView.as_view()),
    path("products/<int:pk>/", apis.ProductDetailView.as_view()),
]
