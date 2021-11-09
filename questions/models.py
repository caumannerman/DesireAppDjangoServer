import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Question(models.Model):
    class QuestionCategory(models.TextChoices):
        UIUX = 'UU', _('UIUX')
        BIBX = 'BB', _('BIBX')
        JS = 'JS', _('제품&산업')
        TS = 'TS', _('툴 사용')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    question_text = models.CharField(max_length=200)
    category = models.CharField(
        max_length=10,
        choices=QuestionCategory.choices,
        default=QuestionCategory.UIUX
    )
    created_on = models.DateTimeField(
        verbose_name=_('작성 시각'),
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        verbose_name=_('수정 시각'),
        auto_now=True
    )

    def __str__(self):
        return self.title
