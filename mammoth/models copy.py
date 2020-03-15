from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#======== this two below is for comment ======================
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

#=================================================
#=================Pattern model===================
#=================================================
class Pattern(models.Model):
    TITLE_MAX_LENGTH = 128

    title = models.CharField(max_length=TITLE_MAX_LENGTH, default='pattern_name')
    slug = models.SlugField(blank=True)
    picture = models.ImageField(upload_to='pattern_images')

    #author = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField(default=" ")

    # change foreign key to OneToOneField
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Pattern, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

#=================================================
#=================comment model===================
#=================================================
class Comment(models.Model):
    # content_type refers to that which object does a comment belong to
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    #  object_id refers to that the object id of a comment belong to
    object_id = models.PositiveIntegerField()
    # this means that comment will be related to any type
    content_object = GenericForeignKey('content_type','object_id') 
    
    # comment rated
    comment_rate = models.IntegerField()

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class Meta:
        ordering = ['-comment_time'] # lasted comment will be the first

# class Comment(models.Model):
#     COMMENT_MAX_LENGTH = 1500

#     pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     text = models.TextField(max_length=COMMENT_MAX_LENGTH)
#     rating = models.IntegerField()
#     time = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-time'] # latest comment will be shown first
