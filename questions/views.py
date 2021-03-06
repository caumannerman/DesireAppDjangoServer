from django_filters.filters import BaseInFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from questions.models import Question
from questions.serializers import QuestionListRetrieveSerializer, QuestionSerializer
from core.permissions import OwnerPermission


class QuestionFilter(FilterSet):
    categories__name__in = BaseInFilter(
        field_name='categories__name', lookup_expr='in')

    class Meta:
        model = Question
        fields = ['user__id', 'categories__name__in', ]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_class = QuestionFilter
    search_fields = ['title', 'question_text', ]
    ordering_fields = ['created_on', ]
    permission_classes = [OwnerPermission]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return QuestionListRetrieveSerializer
        else:
            return QuestionSerializer
