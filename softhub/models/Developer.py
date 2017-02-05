from django.db import models
# from django.contrib.auth.models import User
from .User import User


class Developer(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
