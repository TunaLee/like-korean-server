# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from like_korean.bases.models import Model


class Category(Model):

    name = models.TextField(_('카테고리명'), unique=True)
    eng_name = models.TextField(_('카테고리 영문명'), unique=True)
    class Meta:
        verbose_name = verbose_name_plural = _('강좌 카테고리')
        db_table = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name
