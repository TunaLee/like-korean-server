# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from han_duck.bases.models import Model


class Nationality(Model):
    name = models.TextField(_('국적명'), unique=True)
    eng_name = models.TextField(_('국적명(영어)'), unique=True)


    class Meta:
        verbose_name = verbose_name_plural = _('국적')
        db_table = 'nationalities'
        ordering = ['name']
