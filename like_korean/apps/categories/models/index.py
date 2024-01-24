# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from han_duck.bases.models import Model


class Category(Model):

    name = models.TextField(_('카테고리명'), unique=True)
    eng_name = models.TextField(_('카테고리 영문명'), unique=True)
    class Meta:
        verbose_name = verbose_name_plural = _('강의 카테고리')
        db_table = 'categories'
        ordering = ['name']
