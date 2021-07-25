from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
    

# Create your models here.

class Post(models.Model):
  Ingredients = models.TextField()
  Recipe = models.TextField() 
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
  comment = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)

class UserProfile(models.Model):
  user = models.OneToOneField(User, primary_key=True, verbose_name=("user"), on_delete=models.CASCADE)
  name = models.CharField(blank=True,null=True, max_length=50)
  bio = models.TextField(blank=True,null=True, max_length=500)
  birth_date = models.DateField(blank=True,null=True)
  picture = models.ImageField( upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png')
   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()
    
