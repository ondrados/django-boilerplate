from django.db import models
from django.utils import timezone

from .managers import BaseManager


class BaseModel(models.Model):

    time_created = models.DateTimeField(auto_now_add=True, null=True)
    time_updated = models.DateTimeField(auto_now=True, editable=False, null=True)
    time_deleted = models.DateTimeField(editable=False, null=True)

    published = models.BooleanField(default=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, soft=True, *args, **kwargs):
        if soft:
            self.published = False
            self.time_deleted = timezone.now()
            self.save()
        else:
            super().delete()
