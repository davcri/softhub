from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse

from softhub.models.Application import Application


class SearchView(TemplateView):
    """(SearchView description)"""

    template_name = 'softhub/search/search.html'

    def dispatch(self, *args, **kwargs):
        if not self.request.GET.get('q'):  # if the query string is empty
            return redirect(reverse('softhub:index'))

        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q')
        context['apps'] = self.searchApplications(
            context['search_query'])

        return context

    def searchApplications(self, query):
        app_list = []
        description_match = Application.objects.filter(
            description__contains=query)
        name_match = Application.objects.filter(name__contains=query)
        category_match = Application.objects.filter(
            category__name__contains=query)
        developer_match = Application.objects.filter(
            developer__user__username__contains=query)

        app_list.extend(name_match)
        app_list.extend(description_match)
        app_list.extend(category_match)
        app_list.extend(developer_match)

        return set(app_list)
