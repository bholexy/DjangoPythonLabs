from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    title = RichTextUploadingField(blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)
    image_one = models.FileField(blank=True, null=True)
    text_one = models.CharField(max_length=200, blank=True, null=True)
    image_two = models.FileField(blank=True, null=True)
    text_two = models.CharField(max_length=200, blank=True, null=True)
    image_three = models.FileField(blank=True, null=True)
    text_three = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=40, default='', blank=True)

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return self.title