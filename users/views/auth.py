from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from users.models import NewUser
from users.serializers import UserSerializer, LoginSerializer
from users.services import auth_custom_user, delete_tokens


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    def get_serializer_class(self):
        serializer_class = UserSerializer
        if self.action == 'login':
            serializer_class = LoginSerializer

        return serializer_class

    @action(methods=['post'], detail=False, url_path='login')
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, token = auth_custom_user(
            serializer.validated_data.get('email'),
            serializer.validated_data.get('password'),
        )
        responce = dict()
        responce['user_data'] = UserSerializer(instance=user).data
        responce['token'] = token

        return Response(data=responce, status=status.HTTP_200_OK)

    def logout(self, request, *args, **kwargs):
        try:
            token = request.Meta.get('HTTP_AUTHORIZATION')
            delete_tokens(request.user, token, False)
        except:
            raise ValidationError("ERROR: User not found! Try with another token!")
        logout(request)

        return Response(
            data={'details': 'User token deleted!'},
            status=status.HTTP_200_OK
        )



