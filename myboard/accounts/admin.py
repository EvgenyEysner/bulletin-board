from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html  # для отображения фото в админке
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def avatar(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;"/>'.format(obj.avatar.url))
    avatar.short_description = 'изображение'

    list_display = ['user', 'birthdate', 'avatar', 'first_name', 'last_name', 'email']