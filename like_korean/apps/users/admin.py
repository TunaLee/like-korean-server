# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Local
from django.utils.html import format_html

from template.apps.users.models import User
from template.bases.admin import Admin


@admin.register(User)
class UserAdmin(Admin, UserAdmin):
    list_display = ('profile_image_tag', 'email', 'username', 'phone', 'auth_token', 'is_staff')
    search_fields = ('email', 'username', 'phone')
    list_filter = ()
    ordering = ('-created',)

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="100px;"/>'.format(obj.profile_image.url))

    profile_image_tag.short_description = '프로필'

    fieldsets = (
        ('1. 정보', {'fields': ('id', 'email', 'username', 'phone', 'password', 'auth_token')}),
        ('2. 이미지', {'fields': ('profile_image_tag', 'profile_image', 'profile_image_url')}),
        ('3. 권한', {'fields': ('is_staff',)}),
        ('4. 생성일 / 수정일', {'fields': ('created', 'modified')}),
    )

    add_fieldsets = (
        ('1. 정보', {'fields': ('email', 'username', 'phone', 'password1', 'password2')}),
        ('2. 이미지', {'fields': ('profile_image',)}),
        ('3. 권한', {'fields': ('is_staff',)}),
        ('4. 생성일 / 수정일', {'fields': ('created', 'modified',)}),
    )

    readonly_fields = ('auth_token', "created", "modified", 'profile_image_tag', 'profile_image_url')
