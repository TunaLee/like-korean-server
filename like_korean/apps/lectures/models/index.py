# Python
import os
from time import strftime, gmtime

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from like_korean.apps.lectures.models.mixins_lecture.image import LectureImageModelMixin
from like_korean.apps.lectures.models.mixins_lecture_video.view import LectureVideoViewModelMixin
from like_korean.bases.models import Model


def file_path(path, filename):
    time = strftime("%Y%m%dT%H%M%S", gmtime())
    ext = filename.split('.')[-1]
    filename = f'{time}.{ext}'
    return os.path.join(path, filename)


def lecture_video_path(instance, filename):
    return file_path('Lecture/Video/', filename)


def video_thumbnail_image_path(instance, filename):
    return file_path('Lecture/Video/ThumbnailImage/', filename)


def detail_thumbnail_image_path(instance, filename):
    return file_path('Lecture/DetailImage/ThumbnailImage/', filename)


def lecture_image_path(instance, filename):
    return file_path('Lecture/DetailImage/', filename)


class Unit(Model):
    name = models.TextField(_('단원 명'))
    description = models.TextField(_('단원 설명'), blank=True, null=True)
    _lecture_id = models.SmallIntegerField(_('강좌 id'), blank=True, null=True)

    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE, related_name='units')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='units')

    class Meta:
        verbose_name = verbose_name_plural = _('강좌 단원')
        db_table = 'units'
        ordering = ['-created']


class Lecture(Model,
              LectureImageModelMixin):
    name = models.TextField(_('강좌 이름'), null=True, blank=True)
    description = models.TextField(_('강좌 설명'), null=True, blank=True)
    price = models.DecimalField(_('강좌 비용'), null=True, blank=True, decimal_places=2, max_digits=10)
    _owner_id = models.PositiveSmallIntegerField(_('강사 id'), null=True, blank=True)
    owner_email = models.EmailField(_('강사 email'), null=True, blank=True)

    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='lectures')

    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='lectures')
    language = models.ForeignKey('languages.Language', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='lectures')

    class Meta:
        verbose_name = verbose_name_plural = _('강좌')
        db_table = 'lecture'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        # Set club_name
        if self.category:
            self.category_id = self.category.id

        super(Lecture, self).save(*args, **kwargs)

        # Update related objects
        self.lecture_videos.exclude(is_active=self.is_active).update(is_active=self.is_active)
        self.units.exclude(is_active=self.is_active).update(is_active=self.is_active)

        self.lecture_videos.exclude(lecture_name=self.name).update(lecture_name=self.name)


class LectureVideo(Model,
                   LectureVideoViewModelMixin):
    lecture = models.ForeignKey('Lecture', verbose_name=_('강좌'), on_delete=models.CASCADE,
                                related_name='lecture_videos')
    unit = models.ForeignKey('Unit', verbose_name=_('단원'), on_delete=models.CASCADE, related_name='lecture_videos')

    _lecture_id = models.PositiveSmallIntegerField(_('강좌 id'), blank=True, null=True)
    lecture_name = models.TextField(_('강좌명'), blank=True, null=True)
    unit_name = models.TextField(_('단원명'), blank=True, null=True)

    name = models.TextField(_('영상 제목'), null=True, blank=True)
    description = models.TextField(_('영상 설명'), null=True, blank=True)
    video = models.FileField(_('비디오'), upload_to=lecture_video_path)
    video_url = models.URLField(_('비디오 URL'), null=True, blank=True)
    thumbnail_image = models.ImageField(_('썸네일 이미지'), null=True, blank=True, upload_to=video_thumbnail_image_path)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('강의 비디오')
        db_table = 'lecture_videos'
        ordering = ['-created']

    def __str__(self):
        return f'{self.lecture}'


class LectureImage(Model):
    lecture = models.ForeignKey('Lecture', verbose_name=_('강좌'), on_delete=models.CASCADE,
                                related_name='lecture_images')
    image = models.ImageField(_('이미지'), upload_to=lecture_image_path)
    image_url = models.URLField(_('이미지 URL'), null=True, blank=True)
    thumbnail_image = models.ImageField(_('썸네일 이미지'), null=True, blank=True, upload_to=detail_thumbnail_image_path)
    thumbnail_image_url = models.URLField(_('썸네일 이미지 URL'), null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _('강좌 이미지')
        db_table = 'lecture_images'
        ordering = ['-created']

    def __str__(self):
        return self.id
