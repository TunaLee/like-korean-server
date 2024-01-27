# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Class Section
class LectureVideoViewModelMixin(models.Model):
    view_count = models.IntegerField(_('조회수'), default=0)

    class Meta:
        abstract = True
