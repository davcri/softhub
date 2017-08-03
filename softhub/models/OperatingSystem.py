from django.db import models
from django.core.exceptions import ValidationError

from softhub.models.Executable import Executable
from softhub.models.Version import Version
from softhub.models.Application import Application


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

    family = models.CharField(
        max_length=200,
        unique=True,
        choices=SUPPORTED_OPERATING_SYSTEMS
    )

    def __str__(self):
        return self.family

    @staticmethod
    def getAppsForOS(os):
        """ Returns a QuerySet containing applications with executables for
        the given operating system.

        Arguments
        ----------
        os : a string representing the operating system
        """

        os_obj = OperatingSystem.objects.get(family=os)
        executables = Executable.objects.filter(release_platform=os_obj)
        versions = Version.objects.filter(version_executable=executables)
        apps = Application.objects.filter(version=versions)

        return apps
