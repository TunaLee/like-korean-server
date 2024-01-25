from django.contrib import admin

# Local
from like_korean.apps.nationalities.models.index import Nationality
from like_korean.bases.admin import Admin


@admin.register(Nationality)
class NationalityView(Admin):
    list_display = ('name', 'notation_name')
    search_fields = ('name', 'notation_name')

    fieldsets = (
        ("정보", {"fields": ('name', 'notation_name')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'notation_name')}),
    )
