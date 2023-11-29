from django.urls import path, re_path
from djoser.views import UserViewSet

from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
)

urlpatterns_auth = [
    re_path(
        r"^o/(?P<provider>\S+)/$",
        CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
    path("jwt/create/", CustomTokenObtainPairView.as_view()),
    path("jwt/refresh/", CustomTokenRefreshView.as_view()),
    path("jwt/verify/", CustomTokenVerifyView.as_view()),
    path("logout/", LogoutView.as_view()),
]

urlpatterns_users = [
    path("me/", UserViewSet.as_view({"get": "me"})),
    path("register/", UserViewSet.as_view({"post": "create"})),
    path("activation/", UserViewSet.as_view({"post": "activation"})),
    path("activation-resend/", UserViewSet.as_view({"post": "resend_activation"})),
    path("reset-password/", UserViewSet.as_view({"post": "reset_password"})),
    path("reset-password-confirm/", UserViewSet.as_view({"post": "reset_password_confirm"})),
    path("change-password/", UserViewSet.as_view({"post": "set_password"})),
]
