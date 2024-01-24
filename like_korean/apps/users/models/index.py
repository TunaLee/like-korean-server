# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Bases
from template.bases.models import Model

# Manager
from template.apps.users.models.managers.objects import UserMainManager
from template.apps.users.models.managers.active import UserActiveManager

# Fields
from template.apps.users.models.fields.phone_number import CustomPhoneNumberField


# Class Section
class User(AbstractUser,
           Model):
    email = models.EmailField(_('이메일'), unique=True, null=True, blank=True)
    username = models.CharField(_('닉네임'), unique=True, max_length=100, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)

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
        self.posts.exclude(user_email=self.email).update(user_email=self.email)

        super(User, self).save(*args, **kwargs)


class UserProfile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    type = models.IntegerField(_('유저 타입'), choices=STAFF_TYPE_CHOICES, default=7)

    class Meta:
        verbose_name = verbose_name_plural = _('유저 프로필')
        db_table = 'user_profiles'
        ordering = ['-created']
