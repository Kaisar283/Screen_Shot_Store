from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from users.models import UserToken


class CustomAuthToken(TokenAuthentication):
    def __init__(self):
        super().__init__()

    model = UserToken

    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').filter(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('ERROR: Invalid user token')

        if not token.user.is_active:
            raise AuthenticationFailed("ERROR: User inactive or deleted, please contact with support!")

        return (token.user, token)
