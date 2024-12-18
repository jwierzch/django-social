# dwitter/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import shutil, os, glob, re
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #TODO may need to alter
    avatar = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username
    


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

# Create a Profile for each new user.
#post_save.connect(create_profile, sender=User)

class Dweet(models.Model):
    user = models.ForeignKey(User,
                             related_name="dweets",
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )
    

class gimage(models.Model):
    user = models.ForeignKey(User,
                             related_name="gimage",
                             on_delete=models.DO_NOTHING)
    gimage = models.ImageField(upload_to='gimages/')
    created_at = models.DateTimeField(auto_now_add=True)