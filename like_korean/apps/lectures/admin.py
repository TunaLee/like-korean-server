from django.contrib import admin

# Local
from han_duck.apps.lectures.models.index import Lecture, Unit
from han_duck.bases.admin import Admin


@admin.register(Lecture)
class LectureView(Admin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')
    readonly_fields = ('name', 'description', 'price')

    fieldsets = (
        ("정보", {"fields": ('name', 'description', 'price')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'description', 'price')}),
    )


@admin.register(Unit)
class UnitView(Admin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    readonly_fields = ('name', 'description')

    fieldsets = (
        ("정보", {"fields": ('name', 'description')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'description')}),
    )
