import uuid

from django.db import models

from design_fields.models import DesignField


class UserDesignField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    design_field = models.ForeignKey(DesignField, on_delete=models.CASCADE)
