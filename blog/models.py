from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-published_date"]
        indexes = [
            models.Index(fields=["-published_date"]),
        ]

    def publish(self):
        self.published_date = timezone.now()
        self.save(update_fields=["published_date"])

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title