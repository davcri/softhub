from django.core.management.base import BaseCommand
from django.utils import timezone

from softhub.models.User import User
from softhub.models.Developer import Developer
from .populate_lib.applications import create_applications


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = """
        Populates the db with faked data values.
        Creates Mozilla and Google developers (with password django12) and
        creates applications. Run this only after 'initialize_db' command.
        Set verbose parameter to 2 in order to see errors messages.
    """

    # Path for a folder containing icons to use in order to fake values.
    # I usually use the icons found in
    # /usr/share/icons/hicolor/256x256/apps/
    # Copy them and put in ./assets/icons/
    FAKE_ICONS_PATH = './assets/icons/'
    # FAKE_ICONS_PATH = '/usr/share/icons/hicolor/256x256/apps/'

    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        self.create_common_users()
        create_applications(self.FAKE_ICONS_PATH)

    def printWarning(self, obj1, exception):
        self.stderr.write("WARNING:" + str(obj1) + " not created.")

        if self.verbose:
            self.stdout.write(str(exception))

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
