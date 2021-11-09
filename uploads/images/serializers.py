from rest_framework import serializers

from uploads.images.models import UploadedImage


class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'file', 'name', ]
