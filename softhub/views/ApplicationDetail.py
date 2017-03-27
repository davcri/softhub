from django.views.generic import DetailView

from softhub.models.Application import Application
from softhub.models.Executable import Executable
from softhub.models.Version import Version


class ApplicationDetail(DetailView):
    model = Application
    context_object_name = 'app'
    template_name = 'softhub/application_detail/application_detail_v2.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicationDetail, self).get_context_data(**kwargs)

        # Get the app ID
        app_id = self.get_object().id
        # an alternate method is to get the URL parameter, as explained here:
        # https://stackoverflow.com/questions/15754122/url-parameters-and-logic-in-django-class-based-views-templateview#15754497
        # app_id = self.kwargs['pk']

        context['versions'] = Version.objects.filter(application_id=app_id)
        context['executables'] = Executable.objects.filter(
            version__application_id=app_id)

        return context
