from django.contrib import admin

from chatrooms.models import ChatRoom


@admin.register(ChatRoom)
class ChatRoomModel(admin.ModelAdmin):
    list_filter = ('id', 'user', 'question', 'created_on')
    list_display = ('id', 'user', 'question', 'created_on')
