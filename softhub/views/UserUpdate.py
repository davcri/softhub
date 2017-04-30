from django.views.generic import UpdateView
from django.urls import reverse

from softhub.models.User import User
from softhub.views.UserForm import UserForm


class UserUpdate(UpdateView):
    model = User
    template_name = 'registration/user_update.html'
    # form_class = UserForm
    fields = ['username', 'email']


    def get_success_url(self):
        return reverse('softhub:user_profile')
