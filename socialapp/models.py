from django.db import models

from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save

class User(AbstractUser):

    phone=models.CharField(max_length=10,unique=True)

class Profile(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500, blank=True)

    profile_picture = models.ImageField(upload_to='profiles/',null=True,blank=True,default="profiles/default.png")



class Post(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="posts")

    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    caption = models.TextField(max_length=2200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    liked_by = models.ManyToManyField(User, blank=True)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)


def create_profile(sender,instance,created,**kwargs):

    if created:

        Profile.objects.create(owner=instance)

post_save.connect(User,create_profile)