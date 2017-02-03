from django.forms import ModelForm

from softhub.models.Application import Application
from softhub.models.Developer import Developer


class ApplicationForm(ModelForm):
    def __init__(self, user_id, *args, **kwargs):
        self.user_id = user_id
        super(ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Application
        exclude = ['developer']

    def save(self, commit=True):
        # TODO review this method: do I need to add some error management?
        app = super(ApplicationForm, self).save(commit=False)
        dev = Developer.objects.get(user__id=self.user_id)
        app.developer = dev
        app.save()

        return app
