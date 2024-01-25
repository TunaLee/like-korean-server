from django.contrib import admin

from like_korean.apps.payments.models import Payment
from like_korean.bases.admin import Admin


@admin.register(Payment)
class PaymentView(Admin):
    list_display = ('user_email', 'lecture_name', 'method', 'amount', 'is_active')
    search_fields = ('user_email', 'lecture_name', 'method', 'amount', 'is_active')
    readonly_fields = ('user_email', 'lecture_name', 'amount')

    fieldsets = (
        ("정보", {"fields": ('user', 'lecture', 'method', 'is_active')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('user', 'lecture', 'method', 'is_active')}),
    )
