from rest_framework import serializers

from design_fields.models import DesignField
from design_fields.serializers import DesignFieldSerializer
from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    categories = DesignFieldSerializer(
        many=True, queryset=DesignField.objects.filter())
    answer_count = serializers.IntegerField(
        source='answer_set.count', read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'user', 'title', 'question_text',
                  'categories', 'answer_count', 'created_on', 'updated_on']

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
