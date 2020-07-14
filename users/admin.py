from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Register User model at admin panel
    """

    user_fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "permission",
                    "step",
                )
            },
        ),
    )

    fieldsets = BaseUserAdmin.fieldsets + user_fieldsets

    list_filter = BaseUserAdmin.list_filter

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "permission",
    )