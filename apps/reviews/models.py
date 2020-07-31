from django.db import models
from django.utils import timezone

__all__ = (
    'Review',
)


class Review(models.Model):
    """Review model class definition."""
    author = models.ForeignKey(
        to='users.User',
        on_delete=models.DO_NOTHING,
        related_name='reviews',
    )
    title = models.CharField(max_length=255)
    text = models.TextField(help_text="Required! Min 200 chars.")
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ['-date_created']

    def __str__(self):
        return self.title
