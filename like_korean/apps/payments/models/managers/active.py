# Manager
from like_korean.apps.payments.models.managers.objects import PaymentMainManager


# Class Section
class PaymentActiveManager(PaymentMainManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
