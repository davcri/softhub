from django.views.generic import TemplateView


class UserProfile(TemplateView):
    template_name = 'softhub/user/user.html'
