import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from questions.models import Question

User = get_user_model()


class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE
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
        return 'Chatroom for [Question title] "{}" created by [User email] "{}"'.format(self.question.title, self.user.email)
