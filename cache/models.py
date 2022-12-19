import datetime
import uuid

from django.core.exceptions import FieldError
from django.db import models

# class ArchivedManager(models.Manager):
#     def get_queryset(self):
#         queryset = super(ArchivedManager, self).get_queryset().filter(is_deleted=False)
#         try:
#             qs = queryset.filter(is_archive=True)
#         except FieldError:
#             qs = queryset
#
#         # request = get_request()
#
#         return qs
#
#
# class DeletedManager(models.Manager):
#     def get_queryset(self):
#         qs = super(DeletedManager, self).get_queryset().filter(is_delete=True)
#
#         # request = get_request()
#
#         return qs


class DefaultField(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True)
    date_deleted = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.date_modified = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        self.full_clean()
        super(DefaultField, self).save()
        return super(DefaultField, self).save()

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.date_deleted = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        self.save()
        return


class SocialNetwork(DefaultField):
    social_network = models.CharField(max_length=100)
    css_class = models.CharField(max_length=200, null=True, blank=True, default='')
    title = models.CharField(max_length=200, null=True, blank=True, default='')

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = "Social Networks"

    def __str__(self):
        return self.social_network
