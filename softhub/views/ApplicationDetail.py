from django.views.generic import DetailView
# from django import forms
from django.core.exceptions import PermissionDenied
from django.views.generic import FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

from softhub.models.Application import Application
from softhub.models.Executable import Executable
from softhub.models.Version import Version
from softhub.models.Review import Review
from softhub.views.ReviewForm import ReviewForm
from softhub.views.ReviewUpload import ReviewUpload


class ApplicationDetail(DetailView):
    model = Application
    context_object_name = 'app'
    template_name = 'softhub/application_detail/application_detail.html'

    def post(self, request, *args, **kwargs):
        view = ReviewUpload.as_view()
        return view(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ApplicationDetail, self).get_context_data(**kwargs)
        app = self.get_object()

        # an alternate method is to get the URL parameter, as explained here:
        # https://stackoverflow.com/questions/15754122/url-parameters-and-logic-in-django-class-based-views-templateview#15754497
        # app_id = self.kwargs['pk']

        exes = app.get_latest_executables()
        os_exe_dict = {}
        for e in exes:
            if e.release_platform.family == 'linux':
                context['linux'] = e
            elif e.release_platform.family == 'osx':
                context['osx'] = e
            elif e.release_platform.family == 'windows':
                context['windows'] = e

        context['versions'] = Version.objects.filter(application_id=app.id)
        context['executables'] = Executable.objects.filter(
            version__application_id=app.id)

        context['form'] = ReviewForm()
        context['reviews'] = \
            Review.objects.filter(
                application=self.get_object()).order_by('-date')
        if self.request.user.is_authenticated():
            context['user_reviewed_app'] = \
                Review.userReviewedApplication(self.request.user, app)

        context['apps'] = Application.getRecommendedApps(self.object)

        return context
