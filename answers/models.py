import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from questions.models import Question
from uploads.audios.models import UploadedAudio
from uploads.images.models import UploadedImage
from uploads.files.models import UploadedFile
from uploads.videos.models import UploadedVideo

User = get_user_model()


class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    uploaded_audio = models.ForeignKey(
        UploadedAudio, on_delete=models.SET_NULL, null=True)
    uploaded_image = models.ForeignKey(
        UploadedImage,  on_delete=models.SET_NULL, null=True)
    uploaded_file = models.ForeignKey(
        UploadedFile, on_delete=models.SET_NULL, null=True)
    uploaded_video = models.ForeignKey(
        UploadedVideo,  on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(
        verbose_name=_('작성 시각'),
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        verbose_name=_('수정 시각'),
        auto_now=True
    )

    def __str__(self):
        return self.content
