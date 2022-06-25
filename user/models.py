from cv2 import resize
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.forms import ImageField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)    #call the Base or Parent class to save data to database

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

            # to crop image with Pilliow
            # image = Image.open('demo_image.jpg')
            # box = (200, 300, 700, 600)    box coordinates are (left, upper, right, lower)
            # cropped_image = image.crop(box)
            # cropped_image.save('cropped_image.jpg')

    
#   Setting up signals to listen to the event of the model.save() method is triggered
#   then the receiver fires some actions - create and save users profile
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
