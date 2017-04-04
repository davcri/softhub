from django.db import models
from django.core.exceptions import ValidationError


class OperatingSystem(models.Model):
    # name = models.CharField(max_length=200)
    # release_date = models.DateTimeField('Release date')

    # TODO model validation for this!
    # at the moment validation is done only via Form validation! (because of
    # django's design)
    #
    SUPPORTED_OPERATING_SYSTEMS = (
        ('linux', 'Linux'),
        ('windows', 'Windows'),
        ('osx', 'OSx')
    )
    family = models.CharField(max_length=200, unique=True, choices=SUPPORTED_OPERATING_SYSTEMS)

    def __str__(self):
        return self.family
