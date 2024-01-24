from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LecturesConfig(AppConfig):
    name = "han_duck.apps.lectures"
    verbose_name = _('강의 관리')
