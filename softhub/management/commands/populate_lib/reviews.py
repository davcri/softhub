from softhub.models.Application import Application
from softhub.models.Review import Review
from softhub.models.Rating import Rating
from softhub.models.User import User

from faker import Faker
import random


def create_reviews():
    apps = Application.objects.all()
    fake = Faker()

    user = User.objects.last()

    for app in apps:
        review_count = random.choice(range(4, 20))

        for review in range(review_count):

            rating = Rating.objects.last()

            Review.objects.create(
                text = fake.words(nb=10),
                application = app,
                user = user,
                rating = rating,
            )
