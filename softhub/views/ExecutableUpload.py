from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView

from softhub.models.Executable import Executable
from softhub.views.ExecutableForm import ExecutableForm
from softhub.models.Application import Application
from softhub.models.Version import Version


class ExecutableUpload(CreateView):
    model = Executable
    form_class = ExecutableForm
    template_name = 'softhub/executable_form/executable_form.html'

    def get_context_data(self, **kwargs):
        """ Add 'app' to the context template's variables """

        context = super(ExecutableUpload, self).get_context_data(**kwargs)
        context['app'] = self.get_object()

        return context

    def get_form(self):
        """ Override to filter the default queryset

        https://docs.djangoproject.com/en/1.10/ref/class-based-views/mixins-editing/#formmixin
        """

        form_class = self.get_form_class()
        form = form_class(**self.get_form_kwargs())

        # TODO check if there is a better way of doing this
        # maybe with another method in ExecutableForm ?
        # https://docs.djangoproject.com/en/1.10/topics/class-based-views/intro/#using-class-based-views
        # def get(self, request):
        #    <view logic>
        #    return HttpResponse('result')
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

    def get_object(self):
        """
        By default get_object() would return an Executable with id equals to
        the <pk> parameter passed from the URL; overriding this method should
        change the object returned.

        Note that the <pk> argument passed from the HTML is equal to app.id.
        """

        app_id = self.kwargs.get('pk')
        return Application.objects.get(id=app_id)

    def get_success_url(self):
        app = self.get_object()
        return reverse('softhub:app_detail', kwargs={'pk': app.id})
