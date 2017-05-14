from django.core.management.base import BaseCommand

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.User import User
from softhub.models.License import License
from softhub.models.Category import Category
from softhub.models.Rating import Rating


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = """
        Initialize the db with common values for operating systems,
        categories, licenses and a superuser. Set verbose parameter to 2 in
        order to see error messages
    """

    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        self.create_os()
        self.create_superuser()
        self.create_licenses()
        self.create_categories()
        self.create_ratings()

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
        username = "admin"
        email = "admin@admin.com"
        password = "admin12"

        try:
            admin = User.objects.create_superuser(
                username=username,
                email=email,
                password=password)
            print("superuser created:", admin)
        except Exception as e:
            self.printWarning(username, e)

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
