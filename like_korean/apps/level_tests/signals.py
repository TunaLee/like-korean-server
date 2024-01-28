# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local
from like_korean.apps.level_tests.models import QuestionImage, QuestionAudio


@receiver(post_save, sender=QuestionImage)
def question_image_post_save(sender, instance, created, **kwargs):
    question_image = QuestionImage.objects.filter(id=instance.id)

    if instance.image:
        question_image.update(image_url=instance.image.url)

    instance.question.update(image_url=instance.image.url)


@receiver(post_save, sender=QuestionAudio)
def question_audio_post_save(sender, instance, created, **kwargs):
    question_audio = QuestionAudio.objects.filter(id=instance.id)

    if instance.audio:
        question_audio.update(audio_url=instance.audio.url)

    instance.question.update(audio_url=instance.audio.url)
