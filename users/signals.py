from django.db.models.signals import post_save
from users.models import User
from django.dispatch import receiver
from users.models import Profile

# This function creates a profile at user creation.
# Basically, when a user is saved, this sends a signal to this receiver
# which initiates this function to create a profile with the instance
# of the user created.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
