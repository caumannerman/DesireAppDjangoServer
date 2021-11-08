from rest_framework.routers import DefaultRouter

from chatmessages.views import ChatMessageViewSet

app_name = 'chatmessages'

router = DefaultRouter()
router.register(r'', ChatMessageViewSet)

urlpatterns = [
] + router.urls
