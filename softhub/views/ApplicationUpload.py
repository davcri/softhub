from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from softhub.models.Application import Application
from softhub.views.ApplicationForm import ApplicationForm


class ApplicationUpload(CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('softhub:index')
    template_name = 'softhub/application_form/application_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # if somebody try to access this URL/view but is not a developer
        if not self.request.user.isDeveloper():
            raise PermissionDenied()
        else:
            return super(CreateView, self).dispatch(request, *args, **kwargs)

    def get_form(self):
        """ Override method to pass user_id parameter to the form
        """
        form_class = self.get_form_class()
        form = form_class(
            user_id=self.request.user.id,
            **self.get_form_kwargs())

        return form
