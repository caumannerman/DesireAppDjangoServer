from rest_framework.routers import DefaultRouter

from uploads.images.views import UploadedImageViewSet

app_name = 'uploadedimages'

router = DefaultRouter()
router.register(r'', UploadedImageViewSet)

urlpatterns = [
] + router.urls
