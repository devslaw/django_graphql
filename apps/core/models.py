from django.db import models
from django.utils import timezone


class AbstractDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.modified = timezone.now()
        return super(AbstractDate, self).save(*args, **kwargs)

    class Meta:
        abstract = True
