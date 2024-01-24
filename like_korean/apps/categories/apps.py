from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    name = "han_duck.apps.categories"
    verbose_name = _('강의 카테고리 관리')
