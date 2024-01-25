from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LanguagesConfig(AppConfig):
    name = "like_korean.apps.languages"
    verbose_name = _('언어 관리')
