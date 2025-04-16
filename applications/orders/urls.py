from django.urls import path
from applications.orders import apis


urlpatterns = [
    path("orders/", apis.OrderView.as_view()),
    path("orderitems/", apis.OrderItemView.as_view()),
    path("orders/<int:pk>/", apis.OrderDetailView.as_view()),
]
