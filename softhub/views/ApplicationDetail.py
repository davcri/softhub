from django.views.generic import DetailView
from django import forms
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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['application', 'user']

    # reviewText = forms.()
    # rating = forms.IntegerField()


class ReviewUpload(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'softhub/application_detail/application_detail.html'

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.get_form())
        return super(ReviewUpload, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """ Adds missing attributes to Review object and raise an exception if
        the user already reviewed the application.
        """
        if Review.userReviewedApplication(
            self.request.user,
            self.get_object()
        ):
            raise Exception(
                'User '
                + str(self.request.user)
                + ' already uploaded a review for '
                + str(self.get_object())
            )

        # self.object is a Review object
        self.object = form.save(commit=False)
        self.object.application = self.get_object()
        self.object.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('softhub:app_detail', kwargs={'pk': self.get_object().pk})
        # return reverse('softhub:index')

    def get_object(self):
        return Application.objects.get(id=self.kwargs.get('pk'))


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
        context['reviews'] = Review.objects.filter(application=self.get_object())
        # context['other_executables'] =

        return context
