from django.forms import ModelForm
from django.forms.widgets import HiddenInput

from softhub.models.Version import Version


class VersionForm(ModelForm):
    class Meta:
        model = Version
        exclude = []

        widgets = {
            'application': HiddenInput()
        }
