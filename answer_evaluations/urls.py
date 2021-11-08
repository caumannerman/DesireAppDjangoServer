from rest_framework.routers import DefaultRouter

from answer_evaluations.views import AnswerEvaluationViewSet

app_name = 'answerevaluations'

router = DefaultRouter()
router.register(r'', AnswerEvaluationViewSet)

urlpatterns = [
] + router.urls
