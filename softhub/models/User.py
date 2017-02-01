from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # def isDeveloper(self):
    #     return False
