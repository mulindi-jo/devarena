
from django.db import models

from cache.models import DefaultField
from users.models import Profile


class Project(DefaultField):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.TextField(max_length=2000, null=True, blank=True)
    source_link = models.TextField(max_length=2000, null=True, blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    project_avatar = models.ImageField(null=True, blank=True, default="default.jpg")
    project_owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
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
