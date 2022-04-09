from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets, status
from rest_framework.response import Response


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(viewsets.ViewSet):

    def login(self, request):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exceptions=True)
        user = User.objects.filter(
            username=login_serializer.validated_data['username'],
            password=login_serializer.validated_data['password']).first()
        if not user:
            return Response({'message': 'Wrong credentials', 'token': ''}, status=status.HTTP_401_UNAUTHORIZED)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token}, status=status.HTTP_200_OK)
