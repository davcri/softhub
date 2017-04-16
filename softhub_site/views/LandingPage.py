from django.views.generic import TemplateView

from softhub.models.Application import Application


class LandingPage(TemplateView):
    template_name = "landing-page/index.html"
    max_apps_to_show = 9

    def get_context_data(self, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)

        # Shows a row of application only if there are 3 apps per row
        # This prevents to show incomplete rows
        apps = Application.objects.all()
        appCount = len(apps)
        fullRowsCount = appCount//3  # integer division
        if appCount < self.max_apps_to_show:
            context['apps'] = apps[:fullRowsCount*3]
        else:
            context['apps'] = apps[:self.max_apps_to_show]

        return context
