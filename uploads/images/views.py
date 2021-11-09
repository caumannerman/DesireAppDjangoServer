from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from uploads.images.models import UploadedImage
from uploads.images.serializers import UploadedImageSerializer


class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.filter()
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UploadedImageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_fields = []
    search_fields = []
    ordering_fields = ['created_at', ]
