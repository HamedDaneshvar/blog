from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset() \
                          .filter(status="published")

class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", _("Draft")),
        ("published", _("Published")),
    )
    title = models.CharField(
        max_length=250,
        verbose_name=_("Title"),
    )
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish',
        verbose_name=_("Slug"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name=_("Author"),
    )
    body = models.TextField(
        verbose_name=_("Body"),
    )
    publish = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Publish Time"),
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="draft",
        verbose_name=_("Status"),
    )

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', 
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day,
                              self.slug,])


    objects = models.Manager() # The default manager
    published = PublishedManager() # Our custom manager

    tags = TaggableManager()