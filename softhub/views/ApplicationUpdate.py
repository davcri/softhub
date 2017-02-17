from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from softhub.models.Application import Application


class ApplicationUpdate(UpdateView):
    model = Application
    fields = ['name', 'description', 'icon']
    # TODO these fields can be changed, but what about the others ?
    # The input form is not showed, but can a malicious user submit raw HTTP
    # data and trick this url ?

    template_name = 'softhub/application_form/application_update_form.html'
    # template_name_suffix = '_update_form'
    success_url = reverse_lazy('softhub:index')
