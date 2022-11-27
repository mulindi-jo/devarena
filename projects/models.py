import datetime
import uuid

from django.core.exceptions import FieldError
from django.db import models


class ArchivedManager(models.Manager):
    def get_queryset(self):
        queryset = super(ArchivedManager, self).get_queryset().filter(is_deleted=False)
        try:
            qs = queryset.filter(is_archive=True)
        except FieldError:
            qs = queryset

        # request = get_request()

        return qs


class DeletedManager(models.Manager):
    def get_queryset(self):
        qs = super(DeletedManager, self).get_queryset().filter(is_delete=True)

        # request = get_request()

        return qs


class DefaultField(models.Model):
    # archived_objects = ArchivedManager()
    # deleted_objects = DeletedManager()

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True
        # app_label = 'Projects'

    def save(self, *args, **kwargs):
        self.date_modified = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        self.full_clean()
        super(DefaultField, self).save()
        return super(DefaultField, self).save()


class Project(DefaultField):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.TextField(max_length=2000, null=True, blank=True)
    source_link = models.TextField(max_length=2000, null=True, blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    project_avatar = models.ImageField(null=True, blank=True, default="default.jpg")
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    # class Meta(object):
    #     app_label = 'Projects'
    #     verbose_name = 'Project'
    #     verbose_name_plural = 'Projects'


class Review(DefaultField):
    VOTE_TYPE = (
        ('UP', 'UP VOTE'),
        ('DOWN', 'DOWN VOTE'),
    )
    review_body = models.TextField(null=True, blank=True)
    vote_value = models.CharField(max_length=30, choices=VOTE_TYPE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} Vote'.format(self.project, self.vote_value)


class Tag(DefaultField):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
