from rest_framework import serializers
from accounts.serializers import UserSerializer

from chatmessages.models import ChatMessage


class ChatMessageListRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ChatMessage
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
