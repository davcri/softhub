from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from softhub.models.Application import Application
from softhub.views.ApplicationForm import ApplicationForm
from softhub.models.Developer import Developer


class ApplicationUpdate(UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'softhub/application_form/application_update_form.html'
    context_object_name = 'app'
    # template_name_suffix = '_update_form'
    # success_url = reverse_lazy('softhub:index')

    def dispatch(self, request, *args, **kwargs):
        appId = kwargs.get('pk')
        app = Application.objects.get(id=appId)
        dev = Developer.objects.get(user_id=request.user)

        # if somebody try to access this URL/view but is not the owner of the
        # app
        if not app.ownedByDev(dev):
            raise PermissionDenied()
        else:
            return super(
                ApplicationUpdate,
                self).dispatch(request, *args, **kwargs)

    def get_form(self):
        """ Override method to pass user_id parameter to the form
        """
        from softhub.views.ApplicationUpload import get_form_with_user_id_kwarg
        return get_form_with_user_id_kwarg(self)
