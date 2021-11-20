import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from chatrooms.models import ChatRoom

User = get_user_model()


class ChatMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(
        verbose_name=_('작성 시각'),
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        verbose_name=_('수정 시각'),
        auto_now=True
    )

    def __str__(self):
        return '[User {} @ Chatroom {}]: {}'.format(self.user.email, self.chatroom, self.content)
