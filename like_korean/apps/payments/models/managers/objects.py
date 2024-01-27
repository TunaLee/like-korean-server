# Bases
from like_korean.bases.models import Manager


# Class Section
class PaymentMainManager(Manager):
    def get_payment_user(self, user):
        if not user:
            return None

        queryset = super(PaymentMainManager, self).get_queryset()
        try:
            if payment := queryset.get(user=user):
                return payment.is_active
        except:
            return False
