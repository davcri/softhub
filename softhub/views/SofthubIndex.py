from django.views.generic import TemplateView

from softhub.models.Category import Category
from softhub.models.Application import Application


class SofthubIndex(TemplateView):
    template_name = 'softhub/index/index.html'

    def get_context_data(self, **kwargs):
        context = super(SofthubIndex, self).get_context_data(**kwargs)

        categories = Category.objects.all()
        categories_apps_dict = {}
        for c in categories:
            app_count_for_category = len(
                Application.objects.filter(category=c))
            categories_apps_dict[c] = app_count_for_category

        context['categories_apps_dict'] = categories_apps_dict
        context['apps'] = Application.objects.all()

        return context
