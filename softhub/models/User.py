from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps

from softhub.models.Review import Review


class User(AbstractUser):

    def isDeveloper(self):
        # lazy loading for Developer class
        # Need to use this because importing Developer class gives an error
        Developer = apps.get_model('softhub', 'Developer')

        try:
            dev = Developer.objects.get(user_id=self.id)
            isDev = True
        except Developer.DoesNotExist:
            isDev = False

        return isDev
