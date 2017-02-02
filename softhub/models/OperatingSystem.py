from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateTimeField('Release date')

    family = models.CharField(max_length=200)
    family.choices = (
        ('linux', 'Linux'),
        ('windows', 'Windows'),
        ('osx', 'OSx')
    )

    # executables = models.ManyToManyField('Executable')
    # executables.blank = True

    def __str__(self):
        return self.name
