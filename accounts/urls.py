from rest_framework import routers

from accounts.views import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = [
] + router.urls
