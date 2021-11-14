from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from chatmessages.models import ChatMessage
from chatmessages.serializers import ChatMessageListRetrieveSerializer, ChatMessageSerializer
from core.permissions import OwnerPermission


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ['user__id', 'chatroom__id']
    search_fields = []
    ordering_fields = ['created_on']
    permission_classes = [OwnerPermission]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ChatMessageListRetrieveSerializer
        else:
            return ChatMessageSerializer
