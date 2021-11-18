from rest_framework import serializers

from accounts.serializers import UserSerializer
from answers.models import Answer
from questions.serializers import QuestionListRetrieveSerializer
from uploads.audios.serializers import UploadedAudioSerializer
from uploads.images.serializers import UploadedImageSerializer
from uploads.files.serializers import UploadedFileSerializer
from uploads.videos.serializers import UploadedVideoSerializer


class AnswerListRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    question = QuestionListRetrieveSerializer()
    uploaded_audio = UploadedAudioSerializer()
    uploaded_image = UploadedImageSerializer()
    uploaded_file = UploadedFileSerializer()
    uploaded_video = UploadedVideoSerializer()

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
