from rest_framework import serializers

from uploads.videos.models import UploadedVideo


class UploadedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedVideo
        fields = ['id', 'file', 'name', ]
