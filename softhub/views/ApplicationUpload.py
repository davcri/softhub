from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from softhub.models.Application import Application
from softhub.views.ApplicationForm import ApplicationForm


class ApplicationUpload(CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('softhub:index')
    template_name = 'softhub/application_form/application_form.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # TODO Note that this should be always True, because of the
        # method_decorator
        if request.user.is_authenticated:
            self.user = request.user
        else:
            pass  # Trigger some exception?

        # if somebody try to access this URL/view but is not a developer
        if not self.user.isDeveloper():
            # uncomment the next line to return only a forbidden page with
            # http code 403
            #
            # self.raise_exception = True
            return self.handle_no_permission()
        else:
            return super(CreateView, self).dispatch(request, *args, **kwargs)

    def get_form(self):
        """ Override method to pass user_id parameter to the form
        """
        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs(), user_id=self.user.id)

        return form
