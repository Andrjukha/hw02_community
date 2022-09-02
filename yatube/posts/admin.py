# from django.conf import settings
from django.contrib import admin
from .models import Group
from .models import Post


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
   # settings.EMPTY_VALUE_DISPLAY
    empty_value_display = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ("pk", "text", "pub_date", "author", "group")
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ("text",)
    # Добавляем возможность фильтрации по дате
    list_filter = ("pub_date",)
    list_editable = ("group",)
    # settings.EMPTY_VALUE_DISPLAY
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
