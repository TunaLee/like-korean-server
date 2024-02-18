from django.db.models.signals import post_save
from django.dispatch import receiver

from like_korean.apps.nationalities.models import Nationality


@receiver(post_save, sender=Nationality)
def nationality_image_post_save(sender, instance, created, **kwargs):
    nationality = Nationality.objects.filter(id=instance.id)

    if instance.image:
        nationality.update(image_url=instance.image.url)
