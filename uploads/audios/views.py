from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from uploads.audios.models import UploadedAudio
from uploads.audios.serializers import UploadedAudioSerializer


class UploadedAudioViewSet(viewsets.ModelViewSet):
    queryset = UploadedAudio.objects.filter()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UploadedAudioSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = []
    search_fields = []
    ordering_fields = ['created_at', ]
