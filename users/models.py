
from django.db import models
from django.contrib.auth.models import User
from cache.models import SocialNetwork, DefaultField


class Profile(DefaultField):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    tech_stack = models.CharField(max_length=100, blank=True, null=True, default='')
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True, unique=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/user-default.png')

    class Meta:
        verbose_name = 'Developer Profile'
        verbose_name_plural = "Developer Profiles"

    def __str__(self):
        return str('{} {}'.format(self.first_name, self.last_name))


class ProfileSocialNetwork(DefaultField):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    social_network = models.ForeignKey(SocialNetwork, on_delete=models.DO_NOTHING)
    profile_url = models.CharField(max_length=1000, null=True, blank=True, default='#')

    class Meta(object):
        verbose_name = 'Profile Social Network'
        verbose_name_plural = "Profile Social Networks"
        unique_together = ('profile', 'social_network')

    def __str__(self):
        return '{} {} ({})'.format(self.profile, self.social_network.social_network, self.profile_url)


class Skill(DefaultField):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Profile Skill'
        verbose_name_plural = "Profile Skills"

    def __str__(self):
        return str(self.name)
