from rest_framework_jwt.views import refresh_jwt_token
from django.urls import path

from .viewsets import UserViewSet


urlpatterns = [
    path('login/', UserViewSet.as_view({'post': 'login'}), name='login'),
    path('refresh-token/', refresh_jwt_token, name='refresh_token'),
]
