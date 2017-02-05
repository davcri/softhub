from django.views.generic import TemplateView

from softhub.models.Application import Application


class LandingPage(TemplateView):
    template_name = "landing-page/index.html"

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['apps'] = Application.objects.all()
        return context
