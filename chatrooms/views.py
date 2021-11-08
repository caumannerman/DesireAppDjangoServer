from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from chatrooms.models import ChatRoom
from chatrooms.serializers import ChatRoomSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ['user__id', 'question__id']
    search_fields = []
    ordering_fields = ['created_on']
    permission_classes = [permissions.AllowAny]
