from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from answers.models import Answer
from answers.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ['user__id', 'question__id']
    search_fields = []
    ordering_fields = ['created_on']
    permission_classes = [permissions.AllowAny]
