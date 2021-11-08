from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = ()
    ordering_fields = ('created_on')
    # filterset_fields = ('user__id')
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
