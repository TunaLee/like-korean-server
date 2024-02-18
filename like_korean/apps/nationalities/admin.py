from django.contrib import admin

# Local
from like_korean.apps.nationalities.models.index import Nationality
from like_korean.bases.admin import Admin


@admin.register(Nationality)
class NationalityView(Admin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

    fieldsets = (
        ("정보", {"fields": ('name', 'code')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'code')}),
    )
