from django.db import models
from django.db.models import Avg

from softhub.models.Rating import Rating


class Review(models.Model):
    # title = models.CharField(max_length=100)
    text = models.TextField()
    application = models.ForeignKey('Application')
    user = models.ForeignKey('User')
    rating = models.ForeignKey(Rating)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return (str(self.application) + ' review by ' + str(self.user))

    @staticmethod
    def userReviewedApplication(user, application):
        """ Returns True if the user already reviewed the application.
        """
        user_reviews = Review.objects.filter(user=user)
        applications_reviewed_by_current_user = \
            user_reviews.values_list('application', flat=True)
        # this link explains the use of flat=True
        # https://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.query.QuerySet.values_list

        user_reviewed_app = False
        if application.id in applications_reviewed_by_current_user:
            user_reviewed_app = True
        return user_reviewed_app

    @staticmethod
    def getAverageRating(application):
        """ Returns the average of all ratings or "None" if
        no review has been published for the given application.
        """
        app_reviews = Review.objects.filter(application=application)
        if app_reviews:  # there is at least one review
            avg_rating = app_reviews.aggregate(Avg('rating'))
            avg_rating = avg_rating.get('rating__avg')
            avg_rating = round(avg_rating, 1)
        else:  # no review
            avg_rating = None
        return avg_rating

    @staticmethod
    def getReviewCount(application):
        """ Return the review count for the given application.
        """
        app_count = len(Review.objects.filter(application=application))
        return app_count

    @staticmethod
    def getReviewsByUser(user):
        """ Return the reviews made by the given user.
        """
        user_reviews = Review.objects.filter(user=user).order_by('-date')
        return user_reviews

    # @staticmethod
    # def getReviewedAppsByUser(user):
    #     """ Return the applications reviewed by the given user.
    #     """
    #     user_reviews = Review.objects.filter(user=user)
    #     return user_reviews
