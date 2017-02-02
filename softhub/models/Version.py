from django.db import models


class Version(models.Model):
    version_string = models.CharField(max_length=100)
    release_date = models.DateField('Release Date')
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return self.application.name + " " + self.version_string
