from django.contrib import admin
from .models import Question

# Register your models here.


@admin.register(Question)
class QuestionModel(admin.ModelAdmin):
    list_filter = ('id', 'title','question_text','category','created_on')
    list_display = ('id', 'title','question_text','category','created_on')