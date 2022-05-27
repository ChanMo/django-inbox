from django.utils.html import format_html
from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)
from .models import Message


class MessageAdmin(ModelAdmin):
    model = Message
    menu_label = '收件箱'
    menu_icon = 'mail'
    menu_order = 300
    list_display = ('show_title', 'show_user', 'is_read', 'created')
    list_filter = ('is_read', 'created')
    search_fields = ('title', 'receiver__username')

    # @admin.display(description='标题')
    def show_title(self, obj):
        return format_html('<b>{}</b>', obj.title)

    show_title.short_description = '标题'


# modeladmin_register(MessageAdmin)
