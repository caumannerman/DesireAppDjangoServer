import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from design_fields.models import DesignField
from design_fields.question_design_fields.models import QuestionDesignField
from uploads.audios.models import UploadedAudio
from uploads.images.models import UploadedImage
from uploads.files.models import UploadedFile
from uploads.videos.models import UploadedVideo

User = get_user_model()


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    question_text = models.CharField(max_length=200)
    categories = models.ManyToManyField(
        DesignField, through=QuestionDesignField)
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
