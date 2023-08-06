import uuid
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings
from datetime import datetime


class FactCheck(models.Model):
    """A rating/explanation on how & why a claim is false."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    headline = models.CharField(
            help_text="A headline for the story (255 character limit)",
            max_length=255,
            blank=True
    )

    deck = models.TextField(blank=True)

    explanation = JSONField(
        blank=True,
        null=True
    )

    cover = models.URLField(
        help_text="An image link to use as the cover and for social.",
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    claim_reviewed = models.ForeignKey(
        'Claim',
        on_delete=models.CASCADE
    )

    is_pinned = models.BooleanField(default=False)

    date_modified = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    publish_date = models.DateField(
        help_text="The date this fact check was published.",
        null=True
    )

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if(self.is_published and self.publish_date is None):
            self.publish_date = datetime.now()

        if(not self.is_published):
            self.publish_date = None

        super().save(*args, **kwargs)
