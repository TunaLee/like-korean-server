from django.contrib import admin
from django.utils.html import format_html

# Local
from like_korean.apps.nationalities.models.index import Nationality
from like_korean.bases.admin import Admin


@admin.register(Nationality)
class NationalityView(Admin):
    list_display = ('name', 'eng_name', 'code', 'nationality_image_tag')
    search_fields = ('name', 'code')

    def nationality_image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100px;"/>'.format(obj.image.url))
    fieldsets = (
        ("정보", {"fields": ('name', 'eng_name', 'code', 'image')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'eng_name', 'code', 'image')}),
    )
