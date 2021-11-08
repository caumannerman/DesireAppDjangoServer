from django.contrib import admin

from answer_evaluations.models import AnswerEvaluation


@admin.register(AnswerEvaluation)
class AnswerEvaluationModel(admin.ModelAdmin):
    list_filter = ('id', 'user', 'answer', 'evaluation', 'created_on', )
    list_display = ('id', 'user', 'answer', 'evaluation', 'created_on', )
