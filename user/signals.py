from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('create user profile function called')
    '''
    Once a user registers, it creates a profile for the user.
    '''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print('save user profile function called')
    
    '''
    Once profile is created for the user, the function saves the created profile for the user.
    '''
    instance.profile.save()     # it saves the profile for the User's instance (object)

    # then go ahead to import this file in the apps.py file
