from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import viewsets

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = ()
    ordering_fields = ('created_on')
    # filterset_fields = ('user__id')
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer