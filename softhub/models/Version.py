from django.db import models


class Version(models.Model):
    version_string = models.CharField(max_length=100)
    release_date = models.DateField('Release Date')
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    license = models.ForeignKey('License',
                                on_delete=models.SET_NULL,
                                null=True)
    license.blank = True

    def __str__(self):
        return self.application.name + " " + self.version_string
