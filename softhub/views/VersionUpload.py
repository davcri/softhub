from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied

from softhub.models.Version import Version
from softhub.views.VersionForm import VersionForm
from softhub.models.Application import Application
from softhub.models.Developer import Developer


class VersionUpload(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'softhub/version_form/version_form.html'

    def get_initial(self):
        """ This method is used to populate the "initial" attribute.

        "initial" contains the data used by the form to initialize its fields.
        """
        initial = {
            'application': self.get_object().id,
            'release_date': timezone.now()
        }

        return initial

    def post(self, request, *args, **kwargs):
        """ If it is the latest version, remove the "latest_version" flag from
        the latest Version object.
        """
        app = self.get_object()
        if request.POST.get('latest_version') == 'on':
            Version.handleLatestVersionUpload(app.id)

        return super().post(request, args, kwargs)

    def get_context_data(self, **kwargs):
        """This method is executed only for GET requests."""

        context = super(VersionUpload, self).get_context_data(**kwargs)
        developer = Developer.objects.get(user=self.request.user)

        app = self.get_object()
        if app.ownedByDev(developer):
            context['app'] = app
        else:
            raise PermissionDenied

        return context

    def get_success_url(self):
        return reverse(
            'softhub:app_detail',
            kwargs={'pk': self.get_object().id}
        )

    def get_object(self):
        app_id = self.kwargs.get('pk')
        return Application.objects.get(id=app_id)
