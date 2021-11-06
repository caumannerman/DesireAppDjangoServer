from django.contrib.auth import get_user_model
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from accounts.permissions import CustomUserPermission
from accounts.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = (CustomUserPermission, )
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter, )
    search_fields = ()
    ordering_fields = ('email', 'date_joined', )
