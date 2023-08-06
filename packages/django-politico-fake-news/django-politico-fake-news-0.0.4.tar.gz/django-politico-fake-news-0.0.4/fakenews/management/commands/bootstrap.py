from django.core.management.base import BaseCommand
from fakenews import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = models.User(
            api_id="12345",
            first_name="Andrew",
            last_name="Briz",
            title="Developer"
        )
        user.save()

        twitter = models.SourceType(
            label="Twitter"
        )
        twitter.save()

        blog = models.SourceType(
            label="Blog"
        )
        blog.save()
