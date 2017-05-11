from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.files import File

from softhub.models.Application import Application
from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.User import User
from softhub.models.Developer import Developer
from softhub.models.License import License
from softhub.models.Category import Category
from softhub.models.Rating import Rating

import os
import random


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "Populates the db with faked data values. " \
        + "Set verbose parameter to 2 in order to see errors messages"
    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        # self.create_os()
        # self.create_superuser()
        # self.create_common_users()
        # self.create_licenses()
        # self.create_categories()
        # self.create_ratings()

        # this probably will not work on Windows or other non-UNIX systems
        home = os.getenv('HOME')
        path = home + "/programming_workspace/exercises/web/django/ASSETS/icons/"
        self.create_applications(path)

    def printWarning(self, obj1, exception):
        self.stderr.write("WARNING:" + str(obj1) + " not created.")

        if self.verbose:
            self.stdout.write(str(exception))

    def create_licenses(self):
        for key, license in License.choices:
            try:
                license = License.objects.create(license=license)
                print("License created", license)
            except Exception as e:
                self.printWarning(license, e)

    def create_superuser(self):
        # TODO add check
        username = "daenn"
        email = "davcri91@gmail.com"
        password = "django12"

        try:
            admin = User.objects.create_superuser(
                username=username,
                email=email,
                password=password)
            print("superuser created:", admin)
        except Exception as e:
            self.printWarning(username, e)

    def create_common_users(self):
        usernames = ["Google", "Mozilla"]
        emails = ["google@gmail.com", "moz@mail.com"]
        pwd = "django12"

        data = list(zip(usernames, emails))

        for (u, m) in data:
            try:
                user = User.objects.create_user(username=u, password=pwd)

                dev = Developer(user=user)
                dev.save()
                self.stdout.write(str(dev) + " created")

            except Exception as e:
                self.printWarning(u, e)

    def create_os(self):
        os_list = []
        linux = OperatingSystem()
        linux.family = 'linux'

        windows = OperatingSystem()
        windows.family = 'windows'

        osx = OperatingSystem()
        osx.family = 'osx'

        os_list.append(linux)
        os_list.append(windows)
        os_list.append(osx)

        for os in os_list:
            try:
                os.save()
                print("OS created", os)
            except Exception as e:
                self.printWarning(os, e)

    def create_categories(self):
        categories_name = [
            'internet',
            'office',
            'education',
            'games',
            'programming',
            'utilities',
            'video',
            'audio',
            'music'
        ]

        for c in categories_name:
            try:
                c = c.title()  # capitalizes first letter of a string
                Category.objects.create(name=c)
                print("Category created: ", c)
            except Exception as e:
                self.printWarning(c, e)

    def create_ratings(self):
        for rating in Rating.choices:
            try:
                Rating.objects.create(value=rating[0])
                print("Rating created: ", rating)
            except Exception as e:
                self.printWarning(rating, e)

    def create_applications(self, path):
        """ This method search inside a given path for icon files and for each
        one of them, creates an Application instance and saves it on the db.
        """
        icons = os.listdir(path)

        for icon in icons:
            with open(path + icon, mode='rb') as icon_file:
                # print(icon_file)
                # print(icon_file.name)
                #
                # print(os.path.basename(icon_file.name))
                # print("=========")

                # TODO FIX this mess of code!

                (app_name, extension) = os.path.splitext(icon)
                a = Application()
                a.name = app_name
                # TODO add a description taken from a faker library
                a.description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

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

                # a.icon = ?

                fd = File(icon_file)
                print(fd)
                # print('a.icon.save(path + icon, fd.read())')
                # print('a.icon.save({} + {}, fd.read())'.format(path, icon))
                #

                a.icon.save(icon, fd, save=False)

                icon_file.close()
                fd.close()

                print(a)
                # print(a.description)
                print(a.category)
                print(a.developer)
                print(a.icon)
                print("===========")
                # a.save()
