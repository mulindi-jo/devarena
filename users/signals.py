from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=User)
def updateProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )
    else:
        user = instance
        profile = Profile.objects.get(user=user)
        profile.email = user.email
        profile.username = user.username
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.save()


