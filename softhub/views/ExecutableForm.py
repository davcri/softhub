from django.forms import ModelForm

from softhub.models.Executable import Executable


class ExecutableForm(ModelForm):
    class Meta:
        model = Executable
        exclude = []
