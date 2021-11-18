from rest_framework import serializers

from accounts.serializers import UserSerializer
from design_fields.models import DesignField
from design_fields.serializers import DesignFieldSerializer
from questions.models import Question
from uploads.audios.serializers import UploadedAudioSerializer
from uploads.images.serializers import UploadedImageSerializer
from uploads.files.serializers import UploadedFileSerializer
from uploads.videos.serializers import UploadedVideoSerializer


class QuestionListRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    categories = DesignFieldSerializer(
        many=True, queryset=DesignField.objects.filter())
    uploaded_audio = UploadedAudioSerializer()
    uploaded_image = UploadedImageSerializer()
    uploaded_file = UploadedFileSerializer()
    uploaded_video = UploadedVideoSerializer()
    answer_count = serializers.IntegerField(
        source='answer_set.count', read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'user', 'title', 'question_text', 'categories',
                  'uploaded_audio', 'uploaded_image', 'uploaded_file', 'uploaded_video',
                  'answer_count', 'created_on', 'updated_on']


class QuestionSerializer(serializers.ModelSerializer):
    categories = DesignFieldSerializer(
        many=True, queryset=DesignField.objects.filter())

    class Meta:
        model = Question
        fields = ['user', 'title', 'question_text', 'categories',
                  'uploaded_audio', 'uploaded_image', 'uploaded_file', 'uploaded_video', ]

    def create(self, validated_data):
        categories_data = []
        if validated_data.get('categories'):
            categories_data = validated_data.pop('categories')
        else:
            raise serializers.ValidationError(
                {'categories': ['This field is required.']}, code=400)

        question = Question.objects.create(**validated_data)

        for category_data in categories_data:
            category_qs = DesignField.objects.filter(
                name__iexact=category_data)
            category = category_qs.first()
            question.categories.add(category)

        question.save()
        return question

    def update(self, instance, validated_data):
        categories_data = []
        if validated_data.get('categories'):
            categories_data = validated_data.pop('categories')
        else:
            raise serializers.ValidationError(
                {'categories': ['This field is required.']}, code=400)

        # 질문 정보 업데이트
        for key, value in validated_data.items():
            setattr(instance, key, value)

        for category_data in categories_data:
            category_qs = DesignField.objects.filter(
                name__iexact=category_data)
            category = category_qs.first()
            instance.categories.add(category)

        instance.save()
        return instance
