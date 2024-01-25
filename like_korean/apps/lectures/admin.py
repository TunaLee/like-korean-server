from django.contrib import admin
from django.utils.html import format_html

# Local
from like_korean.apps.lectures.models.index import Lecture, Unit, LectureVideo
from like_korean.bases.admin import Admin
from like_korean.bases.inlines import StackedInline


class UnitInline(StackedInline):
    model = Unit
    fieldsets = (
        ("Unit", {"fields": ('name', 'description')}),
    )
    extra = 0


class LectureVideoInline(StackedInline):
    model = LectureVideo
    fieldsets = (
        ("LectureVideo", {"fields": ('name', 'description', 'video')}),
    )
    extra = 0


@admin.register(LectureVideo)
class LectureVideoView(Admin):
    list_display = ('_lecture_id', 'name', 'thumbnailVideo_tag', 'description', 'lecture_name', 'unit_name')
    search_fields = ('_lecture_id', 'name', 'description', 'lecture_name', 'unit_name')
    # readonly_fields = ('_lecture_id', 'lecture_name', 'unit_name')
    fieldsets = (
        ("정보", {'fields': ('name', 'description', 'video')}),
    )
    add_fieldsets = (
        ("정보", {'fields': ('name', 'description', 'video')}),
    )

    def thumbnailVideo_tag(self, obj):
        if obj.video:
            return format_html(f'<img src="{obj.thumbnail_image_url}" width="100px;"/>')


@admin.register(Lecture)
class LectureView(Admin):
    list_display = ('owner_email', 'name', 'description', 'price')
    search_fields = ('owner_email', 'name', 'description', 'price')
    readonly_fields = ('owner_email', 'name', 'description', 'price')
    inlines = (UnitInline,)

    fieldsets = (
        ("정보", {"fields": ('name', 'description', 'price', 'owner')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'description', 'price', 'owner')}),
    )


@admin.register(Unit)
class UnitView(Admin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    readonly_fields = ('name', 'description')
    inlines = (LectureVideoInline,)

    fieldsets = (
        ("정보", {"fields": ('name', 'description')}),
    )

    add_fieldsets = (
        ("정보", {"fields": ('name', 'description')}),
    )
