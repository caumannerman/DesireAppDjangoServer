from rest_framework.routers import DefaultRouter

from uploads.files.views import UploadedFileViewSet

app_name = 'uploadedfiles'

router = DefaultRouter()
router.register(r'', UploadedFileViewSet)

urlpatterns = [
] + router.urls
