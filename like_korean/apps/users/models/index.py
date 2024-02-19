# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from like_korean.apps.nationalities.models import Nationality
from like_korean.apps.users.models.fields.phone_number import CustomPhoneNumberField
# Bases

# Manager

# Fields

from like_korean.apps.users.models.managers.active import UserActiveManager
from like_korean.apps.users.models.managers.objects import UserMainManager
from like_korean.apps.users.models.mixins.image import ImageModelMixin
from like_korean.bases.models import Model


# Class Section
class User(AbstractUser,
           ImageModelMixin,
           Model):
    email = models.EmailField(_('이메일'), unique=True, null=True, blank=True)
    username = models.CharField(_('닉네임'), max_length=100, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)

    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    language = models.ForeignKey('languages.Language', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserMainManager()
    active = UserActiveManager()

    class Meta:
        verbose_name = verbose_name_plural = _('유저')
        db_table = 'users'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        # Update related objects
        super(User, self).save(*args, **kwargs)
        self.payments.exclude(user_email=self.email).update(user_email=self.email)


