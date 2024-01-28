from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LevelTestsConfig(AppConfig):
    name = "like_korean.apps.level_tests"
    verbose_name = _('테스트 관리')

    def ready(self):
        try:
            import like_korean.apps.level_tests.signals
        except ImportError:
            pass
