from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from softhub.models.Application import Application
from softhub.models.Version import Version
from softhub.models.Developer import Developer


class VersionUpdate(UpdateView):
    model = Version
    fields = ['version_string', 'release_date']
    # TODO check if django accepts other fields with a crafted HTTP request.
    # These fields can be changed, but what about the others ?
    # The input form is not showed, but can a malicious user submit raw HTTP
    # data and trick this url ?

    template_name = 'softhub/version_form/version_update.html'
    # template_name_suffix = '_update_form'

    def dispatch(self, request, *args, **kwargs):
        appId = kwargs.get('pk')
        self.app = Application.objects.get(version=appId)
        print(self.app, appId)

        dev = Developer.objects.get(user_id=request.user)

        # if somebody try to access this URL/view but is not the owner of the
        # app
        if not self.app.ownedByDev(dev):
            # TODO create a fancy PermissionDenied paged
            raise PermissionDenied()
        else:
            return super(
                VersionUpdate,
                self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('softhub:app_detail', kwargs={'pk': self.app.id})
    # def get_object(self, queryset=None, *args, **kwargs):
    #     version_id = self.kwargs.get('version_id')
    #
    #     return Version.objects.get(application=self.app, id=version_id)
