from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from softhub.views.UserForm import UserForm


class UserCreation(CreateView):
    model = User  # ?
    form_class = UserForm
    template_name = 'registration/user_creation.html'
    success_url = reverse_lazy('softhub:login')
