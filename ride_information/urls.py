from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .api.user import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='auth-refresh-token')
] + router.urls
