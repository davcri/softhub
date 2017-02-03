from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import BooleanField

from softhub.models.Developer import Developer
from softhub.models.User import User


class UserForm(UserCreationForm):
    ''' Subclass of User Creation Form
        https://docs.djangoproject.com/en/1.10/topics/auth/default/#django.contrib.auth.forms.UserCreationForm
    '''

    # Need to override default's UserCreationForm that uses
    # django's User in Meta class.
    # Here we override Meta class with our custom Softhub User
    class Meta:
        model = User
        fields = ("username",)
        # field_classes = {'username': UsernameField}

    developer_check = BooleanField(required=False)

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=True)

        if self.cleaned_data.get('developer_check') is True:
            Developer.objects.create(user_id=user.id)

        # user = super(UserForm, self).save(commit=False)
        # user.set_password(self.cleaned_data["password1"])

        # if commit:
        #     user.save()
        #
        #     if self.cleaned_data.get('developer_check') is True:
        #         Developer.objects.create(user_id=user.id)

        return user
