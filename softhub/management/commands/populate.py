from django.core.management.base import BaseCommand
from softhub.models.OperatingSystem import OperatingSystem
from softhub.models.User import User

from django.utils import timezone


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Populates the db with common initial values'

    def handle(self, *args, **options):
        self.create_os()
        self.create_superuser()

    def create_superuser(self):
        # TODO add check
        username = "daenn"
        email = "davcri91@gmail.com"
        password = "django1234"

        if not User.objects.filter(username=username):
            admin = User.objects.create_superuser(username, email, password)
            print("superuser created:", admin)
        else:
            print("ERROR: no user created.", username, "already exist")

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
            if not OperatingSystem.objects.filter(name=os.name):
                os.save()
                print("OS created", os)
            else:
                print("ERROR: no os created.", os, "already exist")
