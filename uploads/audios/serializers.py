from rest_framework import serializers

from uploads.audios.models import UploadedAudio


class UploadedAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedAudio
        fields = ['id', 'file', 'name', ]
