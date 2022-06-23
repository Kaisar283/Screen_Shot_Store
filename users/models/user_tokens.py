import os

from django.db import models
import binascii
from .user import NewUser


class UserToken(models.Model):
    key = models.CharField(max_length=100, unique= True, verbose_name='User token')
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, verbose_name='user')

    class Meta:
        abstract = False
        verbose_name = 'Token'
        verbose_name_plural = 'Tokens'

    def save(self, *args, **kwargs):
        if self.key is None:
            self.key = self.generate_token()
        return super(UserToken, self).save(*args, **kwargs)

    def generate_token(self):
        return binascii.hexlify(os.urandom(30)).decode()

    def __str__(self):
        return f'{self.user.email} | {self.key}'