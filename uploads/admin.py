from django.contrib import admin

from uploads.audios.models import UploadedAudio
from uploads.videos.models import UploadedVideo
from uploads.files.models import UploadedFile
from uploads.images.models import UploadedImage

admin.site.register(UploadedAudio)
admin.site.register(UploadedFile)
admin.site.register(UploadedImage)
admin.site.register(UploadedVideo)
