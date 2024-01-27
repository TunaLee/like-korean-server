from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentsConfig(AppConfig):
    name = "like_korean.apps.payments"
    verbose_name = _('결제 관리')
