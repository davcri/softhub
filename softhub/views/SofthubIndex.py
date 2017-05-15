from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from softhub.models.Category import Category
from softhub.models.Application import Application


class SofthubIndex(TemplateView):
    template_name = 'softhub/index/index.html'
    APPS_PER_PAGE = 12

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
            app_list = Application.objects.filter(
                category=self.category)
        else:
            app_list = Application.objects.all()

        app_paginator = Paginator(app_list, self.APPS_PER_PAGE)

        page = self.request.GET.get('page')

        try:
            apps = app_paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            apps = app_paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 999), deliver last page of results.
            apps = app_paginator.page(paginator.num_pages)

        # context['best_rated_apps'] = Application.getBestReviewdeApps(3)

        context['apps'] = apps
        return context
