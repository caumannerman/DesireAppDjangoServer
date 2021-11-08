from rest_framework import serializers

from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'user', 'title', 'question_text',
                  'category', 'created_on', 'updated_on']
