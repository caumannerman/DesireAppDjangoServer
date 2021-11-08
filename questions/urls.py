from django.urls import path, include
from .views import QuestionViewSet
from rest_framework.routers import DefaultRouter


app_name = 'questions'

router = DefaultRouter()
router.register(r'', QuestionViewSet)

urlpatterns = [
] + router.urls







