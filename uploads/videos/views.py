from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from uploads.videos.models import UploadedVideo
from uploads.videos.serializers import UploadedVideoSerializer


class UploadedVideoViewSet(viewsets.ModelViewSet):
    queryset = UploadedVideo.objects.filter()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UploadedVideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = []
    search_fields = []
    ordering_fields = ['created_at', ]
