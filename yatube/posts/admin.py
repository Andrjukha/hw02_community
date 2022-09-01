from django.contrib import admin

from yatube.settings import EMPTY_VALUE_DISPLAY
from .models import Group
from .models import Post


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    EMPTY_VALUE_DISPLAY


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "pub_date", "author", "group")
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # Добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    list_editable = ("group",)
    EMPTY_VALUE_DISPLAY


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
