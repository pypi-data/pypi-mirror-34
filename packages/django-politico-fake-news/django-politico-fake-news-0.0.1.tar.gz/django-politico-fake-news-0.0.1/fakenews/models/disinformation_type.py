from django.db import models


class DisinformationType(models.Model):
    """A type of disinformation (e.g. Hoax, Photoshopped Image)."""
    label = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.label
