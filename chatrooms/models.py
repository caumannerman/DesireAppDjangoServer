import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(
        User,
        related_name='sender_chatrooms',
        on_delete=models.CASCADE
    )
    recipient = models.ForeignKey(
        User,
        related_name='recipient_chatrooms',
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
        return 'Chatroom between "{}" and "{}"'.format(self.sender.email, self.recipient.email)
