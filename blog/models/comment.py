from django.db import models
from django.utils.translation import gettext_lazy as _

from .post import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Post")
    )
    name = models.CharField(
        max_length=80,
        verbose_name=_("Name"),
    )
    email = models.EmailField(
        verbose_name=_("Email")
    )
    body = models.TextField(
        verbose_name=_("Body")
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    active = models.BooleanField(
        default=True,
        verbose_name=_("Active"),
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"