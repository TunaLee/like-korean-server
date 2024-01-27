from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LecturesConfig(AppConfig):
    name = "like_korean.apps.lectures"
    verbose_name = _('강좌 관리')
