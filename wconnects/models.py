from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    location = models.CharField(max_length=200, null=True)
    photo = CloudinaryField('image', null=True, blank=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Facebook(models.Model):
    facebook = models.CharField(max_length=200, null=True)
    fpassword = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.facebook

class Instagram(models.Model):
    instagram = models.CharField(max_length=200, null=True)
    ig_password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.instagram

class Twitter(models.Model):
    twitter = models.CharField(max_length=200, null=True)
    tw_password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.twitter

class Wechat(models.Model):
    wechat = models.CharField(max_length=200, null=True)
    we_password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.wechat

class Manage(models.Model):
    name = models.CharField(max_length=200, null=True)
    photo = CloudinaryField('image', null=True)
    location = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    like = models.CharField(max_length=200, default='1k')
    dislike = models.CharField(max_length=200, default='0')
    love = models.CharField(max_length=200, default='2.5k')
    followers = models.CharField(max_length=200, default='5k')

    def __str__(self):
        return self.name

class Dating(models.Model):
    name = models.CharField(max_length=200, null=True)
    photo = CloudinaryField('image', null=True)
    location = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    like = models.CharField(max_length=200, default='1k')
    dislike = models.CharField(max_length=200, default='0')
    love = models.CharField(max_length=200, default='2.5k')
    followers = models.CharField(max_length=200, default='5k')

    def __str__(self):
        return self.name