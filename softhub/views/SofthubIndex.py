from django.views.generic import TemplateView

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.Application import Application


class SofthubIndex(TemplateView):
    template_name = 'softhub/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(SofthubIndex, self).get_context_data(**kwargs)
        context['os_list'] = OperatingSystem.objects.all()
        context['apps'] = Application.objects.all()
        return context
