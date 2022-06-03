from django.db.models.signals import post_save
#this is a signal that gets fired after a model is saved
from django.contrib.auth.models import User
#User is goin to be a sender cause this model will be sending a signal
#We need also to define something called receiver
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
	instance.profile.save()

