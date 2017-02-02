from django.db import models
# from django.contrib.auth.models import User
from .User import User

class Developer(models.Model):
    user = models.OneToOneField(User)
    # name = models.CharField(max_length=200)
    # email = models.EmailField()

    def __str__(self):
        return self.user.username
