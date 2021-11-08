from django.contrib import admin

from chatmessages.models import ChatMessage


class ChatMessageAdmin(admin.ModelAdmin):
    list_filter = ('id', 'user', 'content', 'created_on')
    list_display = ('id', 'user', 'content', 'created_on')


admin.site.register(ChatMessage, ChatMessageAdmin)
