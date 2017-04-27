from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

from softhub.models.Application import Application
from softhub.models.Review import Review
from softhub.views.ReviewForm import ReviewForm


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
        return reverse(
            'softhub:app_detail', kwargs={'pk': self.get_object().pk})

    def get_object(self):
        return Application.objects.get(id=self.kwargs.get('pk'))
