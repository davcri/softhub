from django.db import models


class OperatingSystem(models.Model):
    # name = models.CharField(max_length=200)
    # release_date = models.DateTimeField('Release date')

    family = models.CharField(max_length=200, unique=True)
    family.choices = (
        ('linux', 'Linux'),
        ('windows', 'Windows'),
        ('osx', 'OSx')
    )

    def __str__(self):
        return self.family
