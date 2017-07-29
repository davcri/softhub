from django.core.files import File
from faker import Faker

from softhub.models.Application import Application
from softhub.models.Developer import Developer
from softhub.models.Category import Category

import os
import random


def create_applications(path):
    """ This method search inside a given path for icon files and for each
    one of them, creates an Application instance and saves it on the db.
    """

    icons = os.listdir(path)  # throws FileNotFoundError if path doesn't exist

    if len(icons) == 0:
        raise FileNotFoundError("No file found in {0}".format(path))

    for icon in icons:
        with open(path + icon, mode='rb') as icon_file:
            (app_name, extension) = os.path.splitext(icon)

            a = Application()
            a.name = app_name

            fake = Faker()
            a.description = fake.text()

            # assign a random category (from the ones saved on the db) to the
            # application instance
            categories = Category.objects.all()
            categories_ids = Category.objects.values_list('id', flat=True)
            rnd_category_id = random.choice(categories_ids)
            a.category = Category.objects.get(id=rnd_category_id)

            # assign a random developer (from the ones saved on the db) to the
            # application instance
            devs = Developer.objects.all()
            dev_ids = Developer.objects.values_list('id', flat=True)
            rnd_dev_id = random.choice(dev_ids)
            a.developer = Developer.objects.get(id=rnd_dev_id)

            fd = File(icon_file)

            a.icon.save(icon, fd, save=False)
            a.save()

            icon_file.close()
            fd.close()

            print(a)
            # print(a.description)
            print(a.category)
            print(a.developer)
            print(a.icon)
            print("===========")
