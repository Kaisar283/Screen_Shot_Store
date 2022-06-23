from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import ValidationError
from .models import NewUser, UserToken

def auth_custom_user(email: str, password: str):
    data = {
        'username': email,
        'password': password
    }
    serializer = AuthTokenSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    user_token = UserToken.objects.create(user=user)
    return user, user_token


def delete_tokens(user: NewUser, token: str, all:bool):
    try:
        if all:
            UserToken.objects.filtr(user=user).delete()
        else:
            UserToken.objects.filter(user=user, key=token).delete()
    except:
        raise ValidationError("ERROR: User's token not found!")

