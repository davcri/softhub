from django.core.management.base import BaseCommand

from .populate_lib.reviews import create_reviews


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = """
        Creates reviews for existing apps
    """
    verbose = False

    def handle(self, *args, **options):
        if options['verbosity'] in (2, 3):
            self.verbose = True

        create_reviews()
