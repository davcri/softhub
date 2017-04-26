from django.db import models

from softhub.models.Version import Version
from softhub.models.Executable import Executable
from softhub.models.Review import Review
from softhub.models.Category import Category


def upload_dir(app, filename):
    '''
        The end result will be something like:
            "uploads/applications/Firefox/icons/firefox.png"
    '''

    path = ('applications/' + app.name + '/icons/' + filename)
    # Note: if the file already exist in the same path, django will
    # automatically append a random hash code to the filename!
    return path


class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    website = models.URLField(blank=True)
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)

    icon = models.ImageField(upload_to=upload_dir)
    # icon.blank = True

    def __str__(self):
        return self.name

    def ownedByDev(self, developer):
        return self.developer == developer

    def get_latest_version(self):
        ''' The latest version object'''
        versions = Version.objects.filter(application_id=self.id)

        # TODO improve ugly code
        latest = None
        for v in versions:
            if v.latest_version:
                latest = v
                break

        return latest

    def get_latest_executables(self):
        ''' Executables objects for the latest version of the application '''
        v = self.get_latest_version()
        executables = Executable.objects.filter(version=v)
        return executables

    def get_absolute_url(self):
        """ https://docs.djangoproject.com/en/1.11/ref/models/instances/#get-absolute-url

            This method is used from generic views when "success_url" is not
            setted.
        """
        from django.urls import reverse
        return reverse('softhub:app_detail', kwargs={'pk': self.id})

    def getAverageRating(self):
        return Review.getAverageRating(self)

    def getRoundedAverageRating(self):
        return round(self.getAverageRating())

    def getReviewCount(self):
        return Review.getReviewCount(self)

    # def get_non_latest_executables(self):
    #     q1 = Executable.objects.all()
    #     q2 = self.get_latest_executables()
    #
    #     return
