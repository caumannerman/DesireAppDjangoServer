import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from answers.models import Answer

User = get_user_model()


class AnswerEvaluation(models.Model):
    class AnswerEvaluationType(models.TextChoices):
        NG = 'NG', _('Not good enough')
        OK = 'OK', _('Okay')
        GR = 'GR', _('Great')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    evaluation = models.CharField(
        max_length=10,
        choices=AnswerEvaluationType.choices,
        default=AnswerEvaluationType.OK
    )
    created_on = models.DateTimeField(
        verbose_name=_('작성 시각'),
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        verbose_name=_('수정 시각'),
        auto_now=True
    )
