from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from chatrooms.models import ChatRoom
from chatrooms.serializers import ChatRoomListRetrieveSerializer, ChatRoomCreateUpdateSerializer
from core.permissions import OwnerPermission


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ['sender__id', 'recipient__id']
    search_fields = []
    ordering_fields = ['created_on']
    permission_classes = [OwnerPermission]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ChatRoomListRetrieveSerializer
        else:
            return ChatRoomCreateUpdateSerializer
