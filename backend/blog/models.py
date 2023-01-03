from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from my_site.models import Tag


class Post(models.Model):
    Title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="/images/construction.jpg")
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name='Tags')
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug
            self.slug = slug
        super().save(*args, **kwargs)

