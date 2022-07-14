from django.db import models


class BaseQuerySet(models.QuerySet):
    def public(self, *args, **kwargs):
        kwargs["published"] = True
        kwargs["time_deleted__isnull"] = True
        return self.filter(*args, **kwargs)

    def admin(self, *args, **kwargs):
        kwargs["time_deleted__isnull"] = True
        return self.filter(*args, **kwargs)
