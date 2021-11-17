from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from uploads.files.models import UploadedFile
from uploads.files.serializers import UploadedFileSerializer


class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.filter()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UploadedFileSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = []
    search_fields = []
    ordering_fields = ['created_at', ]
