# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from like_korean.bases.models import Model
from like_korean.utils.file_path import file_path


def nationality_image_path(instance, filename):
    return file_path('Nationality/Image/', filename)


class Nationality(Model):
    name = models.TextField(_('국가명(한글)'), unique=True)
    eng_name = models.TextField(_('국가명(영문)'), null=True, blank=True)
    code = models.TextField(_('국가코드'), null=True, blank=True)
    image = models.ImageField(_('국기 이미지'), upload_to=nationality_image_path, null=True, blank=True)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('국적')
        db_table = 'nationalities'
        ordering = ['name']

    def __str__(self):
        return self.code
