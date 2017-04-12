from django.forms import ModelForm, ValidationError

from softhub.models.Executable import Executable
from softhub.models.OperatingSystem import OperatingSystem


class ExecutableForm(ModelForm):
    class Meta:
        model = Executable
        exclude = []

    def clean(self):
        """ Method ovverride to allow the upload of only one executable for a
        given operating system.
        """
        # TODO this could be handled via AJAX on client side.

        cleaned_data = super().clean()

        release_platform = cleaned_data.get('release_platform')
        version = cleaned_data.get('version')

        executables = Executable.objects.filter(version_id=version.id)

        operating_systems_with_an_executable = list()
        for exe in executables:
            operating_systems_with_an_executable.append(exe.release_platform)

        if release_platform in operating_systems_with_an_executable:
            msg = ('An executable for version=['
                   + str(version) + '] on '
                   + release_platform.__str__()
                   + ' is already stored on the DB')
            self.add_error('release_platform', msg)
