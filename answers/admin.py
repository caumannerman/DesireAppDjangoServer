from django.contrib import admin

from answers.models import Answer


@admin.register(Answer)
class AnswerModel(admin.ModelAdmin):
    list_filter = ('id', 'user', 'question', 'content', 'created_on', )
    list_display = ('id', 'user', 'question', 'content', 'created_on', )
