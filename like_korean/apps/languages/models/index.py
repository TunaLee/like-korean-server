# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from like_korean.bases.models import Model


class Language(Model):
    name = models.TextField(_('언어명'), unique=True)
    notation_name = models.TextField(_('표기명'), blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_plural = _('템플릿')
        db_table = 'like_korean'
        ordering = ['-created']
