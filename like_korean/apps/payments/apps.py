from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TemplatesConfig(AppConfig):
    name = "han_duck.apps.app_templates"
    verbose_name = _('관리')
