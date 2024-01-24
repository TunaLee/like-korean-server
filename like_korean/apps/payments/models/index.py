# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from han_duck.bases.models import Model


class PaymentMethod(Model):
    name = models.TextField(_('결제 방법'), unique=True)

    class Meta:
        verbose_name = verbose_name_plural = _('결제 방법')
        db_table = 'payment_methods'
        ordering = ['-created']

class Payment(Model):
    profile = models.ForeignKey('profiles.Profile', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    method = models.ForeignKey('payments.PaymentMethod', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = verbose_name_plural = _('결제')
        db_table = 'payments'
        ordering = ['-created']
