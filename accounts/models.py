import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email,
                    username=None,
                    password=None,
                    first_name=None,
                    last_name=None,
                    is_active=True,
                    is_staff=False,
                    is_superuser=False,
                    ):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("Password is required")
        user_obj = self.model(
            email=self.normalize_email(username)
        )
        user_obj.set_password(password)  # change user password
        user_obj.username = username
        user_obj.email = email
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username=None, email=None, password=None):
        user = self.create_user(
            username=None,
            email=email,
            password=password,
            first_name="",
            last_name="",
            is_staff=True,
            is_superuser=True,
        )
        return user


class User(AbstractUser):
    # Set None for fields that are not used
    username = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('이메일', unique=True)  # Set unique email
    password = models.CharField('비밀번호', max_length=128, blank=True)
    first_name = models.CharField('이름', max_length=30)
    last_name = models.CharField('성', max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.email)
