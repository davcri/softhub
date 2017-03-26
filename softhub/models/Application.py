from django.db import models


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
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)

    icon = models.ImageField(upload_to=upload_dir)
    icon.blank = True

    def __str__(self):
        return self.name

    def ownedByDev(self, developer):
        return self.developer == developer
