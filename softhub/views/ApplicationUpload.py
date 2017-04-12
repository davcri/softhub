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
        return get_form_with_user_id_kwarg(self)


def get_form_with_user_id_kwarg(obj):
    """ Get the form object and adds a user_id keyword argument; returns the
    form.

    This method is shared by ApplicationUpdate and ApplicationUpload classes.

    Parameters
    ----------
    obj : ApplicationUpload object
    """
    form_class = obj.get_form_class()
    kwargs = obj.get_form_kwargs()
    kwargs['user_id'] = obj.request.user.id
    form = form_class(**kwargs)

    return form
