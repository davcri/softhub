from django.db import models


def upload_dir(executable, filename):
    '''
        The end result will be something like:
            "uploads/applications/Firefox/45/firefox.exe"
    '''

    app_name = executable.version.application.name
    version = executable.version.version_string
    path = ('applications/' + app_name + '/executables/' +
            version + '/' + filename)
    # Note: if the file already exist in the same path, django will
    # automatically append a random hash code to the filename!
    return path


class Executable(models.Model):
    version = models.ForeignKey('Version', on_delete=models.CASCADE,
                                related_name="version_executable")
    release_platform = models.ForeignKey('OperatingSystem')
    info = models.CharField(max_length=200)
    info.blank = True

    executable_file = models.FileField(upload_to=upload_dir)

    def __str__(self):
        platform = self.release_platform.__str__()
        return (self.version.__str__() + ' [' + platform + ']')
