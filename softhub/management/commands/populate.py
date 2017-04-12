from django.core.management.base import BaseCommand
from django.utils import timezone

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.User import User
from softhub.models.Developer import Developer
from softhub.models.License import License
from softhub.models.Category import Category


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "Populates the db with faked data values. " \
        + "Set verbose parameter to 2 in order to see errors messages"
    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        self.create_os()
        self.create_superuser()
        self.create_common_users()
        self.create_licenses()
        self.create_categories()

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
                Category.objects.create(name=c)
                print("Category created")
            except Exception as e:
                self.printWarning(os, e)
