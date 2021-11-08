from rest_framework.routers import DefaultRouter

from chatrooms.views import ChatRoomViewSet

app_name = 'chatrooms'

router = DefaultRouter()
router.register(r'', ChatRoomViewSet)

urlpatterns = [
] + router.urls
