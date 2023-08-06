import savepagenow
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Claim


@receiver(pre_save, sender=Claim)
def update_archive_url(sender, instance, **kwargs):
    prev = sender.objects.filter(pk=instance.pk).first()

    # Existing object
    if prev is not None:
        if instance.canoncial_url == '':
            instance.archive_url = ''
        elif instance.canoncial_url != prev.canoncial_url:
            instance.archive_url = savepagenow.capture_or_cache(
                instance.canoncial_url
            )

    # New object
    else:
        instance.archive_url = savepagenow.capture_or_cache(
            instance.canoncial_url
        )

    if(instance.text == ''):
        instance.text = instance.short_text
