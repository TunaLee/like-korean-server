# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

from like_korean.apps.payments.models.managers.active import PaymentActiveManager
from like_korean.apps.payments.models.managers.objects import PaymentMainManager
# Local
from like_korean.bases.models import Model

PAYMENT_METHOD = Choices(
    ('credit_card', _('Credit Card')),
    ('cash', _('Cash')),
    ('event', _('Event')),
    ('etc', _('etc')),
    ('refund', _('refund'))
)
class Payment(Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    method = models.TextField(choices=PAYMENT_METHOD, default='etc')

    user_email = models.EmailField(_('유저 이메일'), null=True, blank=True)
    lecture_name = models.TextField(_('강좌 이름'), null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    objects = PaymentMainManager()
    active = PaymentActiveManager()

    def save(self, *args, **kwargs):
        # Set club_name
        if self.user:
            self.user_email = self.user.email
        if self.lecture:
            self.lecture_name = self.lecture.name
        super(Payment, self).save(*args, **kwargs)
    class Meta:
        verbose_name = verbose_name_plural = _('결제')
        db_table = 'payments'
        ordering = ['-created']
