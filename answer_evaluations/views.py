from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from answer_evaluations.models import AnswerEvaluation
from answer_evaluations.serializers import AnswerEvaluationSerializer


class AnswerEvaluationViewSet(viewsets.ModelViewSet):
    queryset = AnswerEvaluation.objects.all()
    serializer_class = AnswerEvaluationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ['user__id', 'answer__id', 'evaluation', ]
    search_fields = []
    ordering_fields = ['created_on']
    permission_classes = [permissions.AllowAny]
