import uuid

from django.db import models


class DesignField(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name
