from django.db import models

from softhub.models.User import User
from softhub.models.Rating import Rating
from softhub.models.Application import Application


class Review(models.Model):
    # title = models.CharField(max_length=100)
    text = models.TextField()
    application = models.ForeignKey(Application)
    user = models.ForeignKey(User)
    rating = models.ForeignKey(Rating)

    def __str__(self):
        return (str(self.application) + ' review by ' + str(self.user))
