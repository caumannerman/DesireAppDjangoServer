from django.contrib import admin

from questions.models import Question


@admin.register(Question)
class QuestionModel(admin.ModelAdmin):
    list_filter = ('id', 'title', 'question_text', 'created_on')
    list_display = ('id', 'title', 'question_text', 'created_on')
