from django.db import models


class Rating(models.Model):
    min_value = 1  # value included
    max_value = 5  # value included

    choices = []
    for rating in list(range(min_value, max_value+1)):
        choices.append((rating, str(rating)))

    # TODO setter property or attribute ValidationError
    # https://docs.djangoproject.com/en/1.11/ref/validators/
    value = models.PositiveSmallIntegerField(
        choices=choices,
        unique=True)

    def __str__(self):
        return str(self.value)
