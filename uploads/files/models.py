import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from uploads.utils import get_uploaded_file_path


class UploadedFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to=get_uploaded_file_path)
    created_on = models.DateTimeField(
        verbose_name=_('작성 시각'),
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        verbose_name=_('수정 시각'),
        auto_now=True
    )
