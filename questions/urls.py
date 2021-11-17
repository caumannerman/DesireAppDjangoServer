from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questions.views import QuestionViewSet


app_name = 'questions'

router = DefaultRouter()
router.register(r'', QuestionViewSet)

urlpatterns = [
] + router.urls
