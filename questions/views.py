from django_filters.filters import BaseInFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from questions.models import Question
from questions.serializers import QuestionSerializer
from core.permissions import OwnerPermission


class QuestionFilter(FilterSet):
    categories__name__in = BaseInFilter(
        field_name='categories__name', lookup_expr='in')

    class Meta:
        model = Question
        fields = ['user__id', 'categories__name__in', ]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_class = QuestionFilter
    search_fields = []
    ordering_fields = ['created_on', ]
    permission_classes = [OwnerPermission]
