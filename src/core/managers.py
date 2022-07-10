from django.db import models

from .query import BaseQuerySet


class BaseManager(models.Manager):

    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)

    def public(self, *args, **kwargs):
        return self.get_queryset().public(*args, **kwargs)

    def admin(self, *args, **kwargs):
        return self.get_queryset().admin(*args, **kwargs)
