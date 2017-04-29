from django.views.generic import TemplateView

from softhub.models.Application import Application
from softhub.models.Developer import Developer
from softhub.models.Review import Review


class UserProfile(TemplateView):
    template_name = 'softhub/user/user.html'

    def get_context_data(self):
        context = super().get_context_data()

        user = self.request.user  # user is a SimpleLazyObject
        if user.isDeveloper():
            dev = Developer.objects.get(user_id=user)
            apps = Application.objects.filter(developer=dev)
            context['apps'] = apps

        context['reviewed_apps'] = Review.getReviewsByUser(self.request.user)

        return context
