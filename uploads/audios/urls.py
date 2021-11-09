from rest_framework.routers import DefaultRouter

from uploads.audios.views import UploadedAudioViewSet

app_name = 'uploadedaudios'

router = DefaultRouter()
router.register(r'', UploadedAudioViewSet)

urlpatterns = [
] + router.urls
