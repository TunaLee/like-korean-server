from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CategoriesConfig(AppConfig):
    name = "like_korean.apps.categories"
    verbose_name = _('강좌 카테고리 관리')
