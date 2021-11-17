from rest_framework import serializers

from accounts.serializers import UserSerializer
from chatrooms.models import ChatRoom
from chatmessages.models import ChatMessage
from chatmessages.serializers import ChatMessageSerializer


class ChatRoomListRetrieveSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    recipient = UserSerializer()
    latest_chat_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatRoom
        fields = ['id', 'sender', 'recipient',
                  'latest_chat_message', 'created_on', 'updated_on', ]

    def get_latest_chat_message(self, obj):
        try:
            latest_chat_message = ChatMessage.objects.filter(
                chatroom=obj).order_by('-created_on').first()
            serializer = ChatMessageSerializer(latest_chat_message)
            return serializer.data
        except:
            return None


class ChatRoomCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['sender', 'recipient', ]
