from django.db import models


class Version(models.Model):
    version_string = models.CharField(max_length=100)
    release_date = models.DateField('Release Date')
    application = models.ForeignKey('Application', on_delete=models.CASCADE)
    latest_version = models.BooleanField()

    license = models.ForeignKey('License',
                                on_delete=models.SET_NULL,
                                null=True)
    license.blank = True

    def __str__(self):
        return self.application.name + " " + self.version_string

    @staticmethod
    def handleLatestVersionUpload(app_id):
        """ Should be called when uploading or updating a new Version that is
        the latest.
        Get the current latest version and set its "latest_version" attribute
        to False.
        """
        try:
            v = Version \
                .objects \
                .filter(application_id=app_id) \
                .get(latest_version=True)
            v.latest_version = False
            v.save()
        except Version.DoesNotExist:
            print("Nothing to do")
