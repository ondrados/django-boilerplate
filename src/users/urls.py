from django.urls import path, re_path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views


urlpatterns_auth = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', views.RegisterAPIView.as_view(), name='auth_register'),
    # re_path(r'^password-reset/', include('django_rest_passwordreset.urls', namespace='password-reset')),
]

urlpatterns_user = [
    path('me/', views.UserAPIView.as_view(), name='user_detail'),

]
