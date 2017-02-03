from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import BooleanField

from softhub.models.Developer import Developer


class UserForm(UserCreationForm):
    developer_check = BooleanField()

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

            if self.cleaned_data.get('developer_check') is True:
                Developer.objects.create(user_id=user.id)

        return user
