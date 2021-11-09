import os
from django.core.exceptions import ValidationError

uploaded_video_valid_extensions = ['.mov', '.avi', '.mp4', '.webm', '.mkv', ]

uploaded_audio_valid_extensions = ['.mp3', '.wav', 'm4a', '.ogg', ]


def validate_video_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path + filename
    if not ext.lower() in uploaded_video_valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_audio_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path + filename
    if not ext.lower() in uploaded_audio_valid_extensions:
        raise ValidationError('Unsupported file extension.')
