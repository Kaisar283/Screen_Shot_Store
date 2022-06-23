from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50, required=True, help_text='Электронная почта')
    password = serializers.CharField(max_length=100, required=True, help_text='Пароль')

    