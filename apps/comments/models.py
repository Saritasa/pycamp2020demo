from django.db import models
from django.utils import timezone

__all__ = (
    'Comment',
)


class Comment(models.Model):
    """Comment model class definition."""
    author = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    review = models.ForeignKey('reviews.Review', on_delete=models.DO_NOTHING)
    text = models.TextField()
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return f"{self.id} -- {self.date_created}"
