from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'receiver', 'is_read', 'created')
    list_per_page = 12
    list_filter = ('is_read', 'created')
    search_fields = ('title', 'receiver__username', 'body')
    raw_id_fields = ('receiver',)
