from django.urls import reverse_lazy
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
    success_url = reverse_lazy('softhub:index')
    template_name = 'softhub/version_form/version_form.html'

    # This method is used to populate the "initial" attribute
    # "initial" contains the data used by the form to initialize its fields.
    def get_initial(self):
        application = self.request.GET.get('app', '')
        initial = {
            'application': application,
            'release_date': timezone.now()
            }
        return initial

    def post(self, request, *args, **kwargs):
        # If it is the latest version, remove the "latest_version" flag from
        # the latest Version object.
        if request.POST.get('latest_version') == 'on':
            try:
                v = Version.objects.get(latest_version=True)
                v.latest_version = False
                v.save()
            except Version.DoesNotExist:
                pass

        return super().post(request, args, kwargs)

    def get_context_data(self, **kwargs):
        # This method is executed only for GET requests.
        context = super(VersionUpload, self).get_context_data(**kwargs)
        developer = Developer.objects.get(user=self.request.user)

        id = self.request.GET.get('app', '')
        if id:
            app = Application.objects.get(id=id)
            if app.ownedByDev(developer):
                context['app'] = app
            else:
                raise PermissionDenied

        else:
            raise Exception("Version Upload: no application specified." +
                            "Missing id parameter in query string")

        return context
