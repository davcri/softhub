from django.core.management.base import BaseCommand

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

    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        try:
            self.create_common_users()
            create_applications(self.FAKE_ICONS_PATH)
        except FileNotFoundError as err:
            self.stderr.write(
                "{0}. ".format(str(err))
                + "Copy icons in the path specified and re-run this command"
                + "If you are on a Linux, try something like this:\n"
                + "> cp /usr/share/icons/hicolor/128x128/apps/* ./assets/icons"
                )

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
                self.stdout.write("User created: {0}".format(str(dev)))

            except Exception as e:
                self.stderr.write(
                    "WARNING: {0} User, {1}".format(u, str(e))
                )
