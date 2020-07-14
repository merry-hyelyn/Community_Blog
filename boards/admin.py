from django.contrib import admin
from boards.models import Board
from django.contrib import admin


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """Register Board model at admin panel"""

    list_display = ("name", "create_user", "path", "created_at", "updated_at")