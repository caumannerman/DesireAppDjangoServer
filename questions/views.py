from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from questions.models import Question
from questions.serializers import QuestionSerializer
from core.permissions import OwnerPermission


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filter_fields = ['user__id']
    search_fields = []
    ordering_fields = ['created_on']
    permission_classes = [OwnerPermission]
