from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from softhub.models.Application import Application
from softhub.models.Developer import Developer


class ApplicationUpdate(UpdateView):
    model = Application
    fields = ['name', 'description', 'icon']
    # TODO check if django accepts other fields with a crafted HTTP request.
    # These fields can be changed, but what about the others ?
    # The input form is not showed, but can a malicious user submit raw HTTP
    # data and trick this url ?

    template_name = 'softhub/application_form/application_update_form.html'
    # template_name_suffix = '_update_form'
    success_url = reverse_lazy('softhub:index')

    def dispatch(self, request, *args, **kwargs):
        appId = kwargs.get('pk')
        app = Application.objects.get(id=appId)
        dev = Developer.objects.get(user_id=request.user)

        # if somebody try to access this URL/view but is not the owner of the
        # app
        if not app.ownedByDev(dev):
            # TODO create a fancy PermissionDenied paged
            raise PermissionDenied()
        else:
            return super(
                ApplicationUpdate,
                self).dispatch(request, *args, **kwargs)
