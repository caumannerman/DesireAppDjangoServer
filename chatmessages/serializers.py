from rest_framework import serializers
from accounts.serializers import UserSerializer

from chatmessages.models import ChatMessage
from uploads.audios.serializers import UploadedAudioSerializer
from uploads.images.serializers import UploadedImageSerializer
from uploads.files.serializers import UploadedFileSerializer
from uploads.videos.serializers import UploadedVideoSerializer


class ChatMessageListRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    uploaded_audio = UploadedAudioSerializer()
    uploaded_image = UploadedImageSerializer()
    uploaded_file = UploadedFileSerializer()
    uploaded_video = UploadedVideoSerializer()

    class Meta:
        model = ChatMessage
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'
