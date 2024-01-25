from django.contrib import admin

# Local
from like_korean.apps.categories.models.index import Category
from like_korean.bases.admin import Admin


@admin.register(Category)
class CategoryView(Admin):
    list_display = ('name', 'eng_name')
    search_fields = ('name', 'eng_name')

    fieldsets = (
        ("정보", {"fields": ('name', 'eng_name')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'eng_name')}),
    )
