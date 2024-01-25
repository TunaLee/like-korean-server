# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from like_korean.bases.models import Model


class Nationality(Model):
    name = models.TextField(_('국적명'), unique=True)
    notation_name = models.TextField(_('표기명'), unique=True)


    class Meta:
        verbose_name = verbose_name_plural = _('국적')
        db_table = 'nationalities'
        ordering = ['name']
