from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NationalitiesConfig(AppConfig):
    name = "like_korean.apps.nationalities"
    verbose_name = _('국적 관리')
