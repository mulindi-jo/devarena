from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from users.models import Profile


@receiver(post_save, sender=User)
def updateProfile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name
        )
    else:
        to_update = False
        profile = Profile.objects.get(user=user)
        if user.first_name != profile.first_name:
            profile.first_name = user.first_name
            to_update = True

        if user.last_name != profile.last_name:
            profile.last_name = user.last_name
            to_update = True

        if user.email != profile.email:
            profile.email = user.email
            to_update = True

        if to_update:
            profile.save()

@receiver(post_save, sender=Profile)
def updateUser(sender, instance, **kwargs):
    to_update = False
    profile = instance
    user = User.objects.get(id=profile.user_id)

    if user.first_name != profile.first_name:
        user.first_name = profile.first_name
        to_update = True

    if user.last_name != profile.last_name:
        user.last_name = profile.last_name
        to_update = True

    if user.email != profile.email:
        user.email = profile.email
        to_update = True

    if to_update:
        user.save()
