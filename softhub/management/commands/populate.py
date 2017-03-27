from django.core.management.base import BaseCommand
from django.utils import timezone

from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.User import User
from softhub.models.Developer import Developer
from softhub.models.License import License


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "Populates the db with common initial values"
    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        self.create_os()
        self.create_superuser()
        self.create_common_users()
        self.create_licenses()

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

        mint = OperatingSystem()
        mint.name = "Linux Mint 18"
        mint.release_date = timezone.datetime(
            2016, 6, 30, tzinfo=timezone.utc)
        mint.family = "linux"
        os_list.append(mint)

        ubuntu = OperatingSystem()
        ubuntu.name = "Ubuntu 16.04"
        ubuntu.release_date = timezone.datetime(
            2016, 4, 21, tzinfo=timezone.utc)
        ubuntu.family = "linux"
        os_list.append(ubuntu)

        windows7 = OperatingSystem()
        windows7.name = "Windows 7"
        windows7.release_date = timezone.datetime(
            2009, 7, 22, tzinfo=timezone.utc)
        windows7.family = "windows"
        os_list.append(windows7)

        for os in os_list:
            try:
                if OperatingSystem.objects.filter(name=os.name):
                    raise Exception("Operating system already exist")
                os.save()
                print("OS created", os)
            except Exception as e:
                self.printWarning(os, e)
