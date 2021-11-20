import uuid

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext as _

from design_fields.models import DesignField
from design_fields.user_design_fields.models import UserDesignField
from uploads.utils import get_uploaded_file_path


class AccountType(models.TextChoices):
    ME = 'ME', _('Mentee')
    MO = 'MO', _('Mentor')


class CustomUserManager(BaseUserManager):
    def create_user(self, email,
                    username=None,
                    password=None,
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
            is_staff=True,
            is_superuser=True,
        )
        return user


class User(AbstractUser):
    # Set None for fields that are not used
    username = None
    first_name = None
    last_name = None

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('이메일', unique=True)  # Set unique email
    password = models.CharField('비밀번호', max_length=128, blank=True, null=True)
    nickname = models.CharField('닉네임', max_length=30)
    profile_image = models.ImageField(
        upload_to=get_uploaded_file_path, blank=True)
    acc_type = models.CharField(
        '계정 유형', choices=AccountType.choices, default=AccountType.ME, max_length=30)
    design_fields = models.ManyToManyField(
        DesignField, through=UserDesignField)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def __str__(self):
        return '{} ({})'.format(self.email, self.nickname)
