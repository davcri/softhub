from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from softhub.models.Version import Version


class VersionForm(ModelForm):
    class Meta:
        model = Version
        exclude = []

        # TODO check if django accepts other fields with a crafted HTTP request.
        # These fields can be changed, but what about the others ?
        # The input form is not showed, but can a malicious user submit raw HTTP
        # data and trick this url ?
        # Probably this hidden input can be exploited.
        widgets = {
            'application': HiddenInput()
        }
