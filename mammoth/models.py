from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

#======== this two below is for comment ======================
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Pattern(models.Model):
    TITLE_MAX_LENGTH = 128

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    #slug = models.SlugField(blank=True)
    picture = models.ImageField(upload_to='pattern_images')
    #author = models.CharField(max_length=TITLE_MAX_LENGTH)

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        super(Pattern, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

#=================================================
#=================comment model===================
#=================================================
class Comment(models.Model):
    # content_type refers to that which object does a comment belong to
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    #  object_id refers to that which object does a comment belong to
    object_id = models.PositiveIntegerField()
    # this means that comment will be related to any type
    content_object = GenericForeignKey('content_type','object_id') 

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    class Meta:
        ordering = ['-comment_time'] # lasted comment will be the first
