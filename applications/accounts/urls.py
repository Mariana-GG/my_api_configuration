from django.urls import path
from applications.accounts import apis


urlpatterns = [
    path("register/", apis.UserRegistrationView.as_view()),
    path("login/", apis.UserLoginView.as_view()),
    path("users/", apis.ListUsersView.as_view()),
    path("users/<int:pk>/", apis.UserDetailView.as_view()),
]
