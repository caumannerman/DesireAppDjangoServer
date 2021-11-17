from rest_framework.routers import DefaultRouter

from answers.views import AnswerViewSet

app_name = 'answers'

router = DefaultRouter()
router.register(r'', AnswerViewSet)

urlpatterns = [
] + router.urls
