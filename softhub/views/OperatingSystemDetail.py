from django.views.generic import DetailView

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.Executable import Executable


class OperatingSystemDetail(DetailView):
    model = OperatingSystem
    context_object_name = 'os'
    template_name = 'softhub/operatingsystem_detail/operatingsystem_detail.html'
    # TODO how to format here? Try autopep8

    def get_context_data(self, **kwargs):
        context = super(OperatingSystemDetail, self).get_context_data(**kwargs)

        # TODO add try/catch block and check that this is correct!
        platform_id = self.kwargs.get('pk')
        context['packages'] = Executable.objects.filter(
            release_platform__id=platform_id)
        return context
