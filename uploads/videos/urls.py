from rest_framework.routers import DefaultRouter

from uploads.videos.views import UploadedVideoViewSet

app_name = 'uploadedvideos'

router = DefaultRouter()
router.register(r'', UploadedVideoViewSet)

urlpatterns = [
] + router.urls
