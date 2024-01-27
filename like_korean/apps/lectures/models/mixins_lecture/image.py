# Python
import os
from time import strftime, gmtime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


# Function Section
def image_path(instance, filename):
    upload_to = 'Lecture/ThumbnailImage/'
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(upload_to, filename)


# Class Section
class LectureImageModelMixin(models.Model):
    thumbnail_image = models.ImageField(_('썸네일 이미지'), upload_to=image_path, blank=True, null=True)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), blank=True, null=True)

    class Meta:
        abstract = True
