from rest_framework import serializers

from accounts.serializers import UserSerializer
from answers.models import Answer
from questions.serializers import QuestionListRetrieveSerializer


class AnswerListRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    question = QuestionListRetrieveSerializer()

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
