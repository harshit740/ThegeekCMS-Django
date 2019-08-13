import mimetypes

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from util.uniqslug import unique_slug_generator

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)



class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(null=True)
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, )
    tags = models.ManyToManyField(Tag)
    byline = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to='media/blog/images')
    slug = models.SlugField(blank=True,editable=False)
    content = models.TextField()
    is_published = models.BooleanField(choices=STATUS,default=False)
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    publish_on = models.DateField(null=True)
    list_display = ('title', 'category', 'tags', 'author', 'publish_on', 'created_on', 'updated_on')
    search_fields = ['title', 'byline',]
    list_filter = ['publish_on', 'created_on']
    date_hierarchy = 'publish_on'

    class Meta:
        ordering = ['-publish_on','-created_on']

    def __str__(self):
        return self.title




@receiver(models.signals.pre_save, sender=Post)
def auto_slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class PostImage(models.Model):
    auhor = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="public/blog/images/",)
    posted_on = models.DateField(auto_now=True,)
