from django.views.generic import TemplateView

from softhub.models.Category import Category
from softhub.models.Application import Application


class SofthubIndex(TemplateView):
    template_name = 'softhub/index/index.html'

    def __init__(self, **kwargs):
        self.category = None
        super().__init__(**kwargs)  # __init__ defined in View class

    def dispatch(self, request):
        category_name = self.request.GET.get('category')
        if category_name:
            self.category = Category.objects.get(name=category_name)
        return super().dispatch(request)

    def get_context_data(self, **kwargs):
        context = super(SofthubIndex, self).get_context_data(**kwargs)

        categories = Category.objects.all()
        categories_apps_dict = {}
        for c in categories:
            app_count_for_category = len(
                Application.objects.filter(category=c))
            categories_apps_dict[c] = app_count_for_category

        context = {
            'categories_apps_dict': categories_apps_dict
        }

        if self.category is not None:
            context['current_category'] = self.category
            context['apps'] = Application.objects.filter(
                category=self.category)
        else:
            context['apps'] = Application.objects.all()
        return context
