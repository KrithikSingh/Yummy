from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
    

# Create your models here.

class Post(models.Model):
  Title = models.CharField(max_length=50, default="Title")
  image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True)
  Ingredients = models.TextField()
  Recipe = models.TextField() 
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, blank=True, related_name='likes')


class Comment(models.Model):
  comment = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Post', on_delete=models.CASCADE)
  likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
  parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,related_name='+')

  @property
  def children(self):
    return Comment.objects.filter(parent=self).order_by('-created_on').all()

  
  @property
  def is_parent(self):
    if self.parent is None:
      return True
    return False  
class UserProfile(models.Model):
  user = models.OneToOneField(User, primary_key=True, verbose_name=("user"), on_delete=models.CASCADE)
  name = models.CharField(blank=True,null=True, max_length=50)
  bio = models.TextField(blank=True,null=True, max_length=500)
  birth_date = models.DateField(blank=True,null=True)
  picture = models.ImageField( upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png')
  followers = models.ManyToManyField(User, blank= True, related_name='followers')
   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()
    
class Notification(models.Model):
  # 1 = like, 2 = Comment, 3 = Follow
  to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE, null = True)
  from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE, null = True)
  post = models.ForeignKey('Post', on_delete =models.CASCADE, related_name='+', blank=True, null=True)
  comment = models.ForeignKey('Comment', on_delete =models.CASCADE, related_name='+', blank=True, null=True)
  notification_Type = models.IntegerField()
  date = models.DateTimeField(default=timezone.now)
  user_has_seen = models.BooleanField(default=False)