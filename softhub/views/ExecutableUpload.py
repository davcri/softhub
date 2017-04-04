from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

from softhub.models.Executable import Executable
from softhub.views.ExecutableForm import ExecutableForm
from softhub.models.Application import Application
from softhub.models.Version import Version


class ExecutableUpload(CreateView):
    model = Executable
    form_class = ExecutableForm
    success_url = reverse_lazy('softhub:index')
    template_name = 'softhub/executable_form/executable_form.html'

    def get_context_data(self, **kwargs):
        context = super(ExecutableUpload, self).get_context_data(**kwargs)

        if self.request == "GET":
            id = self.request.GET.get('app', '')

            # TODO exceptions
            app = Application.objects.get(id=id)
            context['app'] = app

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
            id = self.request.GET.get('app', '')

            # Filter the Version items inserted in the HTML select tag input,
            # modifying the default queryset that include all the Version
            # objects.
            # Select only the versions of the application id passed via a GET
            # parameter.
            form.fields['version'].queryset = (
                Version.objects.filter(application_id=id))

        return form
