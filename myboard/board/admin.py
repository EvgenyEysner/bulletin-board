from django.contrib import admin
from django.utils.html import format_html  # для отображения фото в админке
from .models import *


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 45px; height:45px;"/>'.format(obj.image.url))
    image_tag.short_description = 'изображение'

    date_hierarchy = 'created'
    list_display = ['name', 'description', 'created', 'image_tag']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__']
