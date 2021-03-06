from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied
from django.urls import reverse

from softhub.models.Executable import Executable
from softhub.models.Developer import Developer
from softhub.models.Version import Version


class ExecutableUpdate(UpdateView):
    model = Executable
    fields = ['version', 'release_platform', 'info', 'executable_file']
    template_name = 'softhub/executable_form/executable_update.html'
    context_object_name = 'executable'

    def dispatch(self, request, *args, **kwargs):
        executableId = kwargs.get('pk')
        executable = Executable.objects.get(id=executableId)
        app = executable.version.application

        dev = Developer.objects.get(user_id=request.user)

        # if somebody try to access this URL/view but is not the owner of the
        # version
        if not app.ownedByDev(dev):
            raise PermissionDenied()
        else:
            return super(
                ExecutableUpdate,
                self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        exe = self.get_object()
        return reverse('softhub:app_detail',
                       kwargs={'pk': exe.version.application.id})

    def get_form(self):
        """ Shows only the current application's versions.
        Override to filter the default queryset
        https://docs.djangoproject.com/en/1.10/ref/class-based-views/mixins-editing/#formmixin
        """

        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())

        if self.request.method == 'GET':
            app = self.get_object()

            # Filter the Version items inserted in the HTML select tag input,
            # modifying the default queryset that include all the Version
            # objects.
            # Select only the versions of the application id passed via a GET
            # parameter.
            form.fields['version'].queryset = (  # TODO change in 'versions'
                Version.objects.filter(application_id=app.id))

        return form
