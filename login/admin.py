from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resource import CustomUserResource
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'is_active')

    def activate_user(self, request, queryset):
        queryset.update(is_active=True)  # 批量激活选中的用户

    activate_user.short_description = "激活选中的用户"

    actions = [activate_user]  # 添加激活用户的操作