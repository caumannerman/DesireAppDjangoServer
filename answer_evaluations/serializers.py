from rest_framework import serializers

from answer_evaluations.models import AnswerEvaluation


class AnswerEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerEvaluation
        fields = '__all__'
