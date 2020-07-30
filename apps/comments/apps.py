from django.apps import AppConfig

__all__ = (
    'CommentsAppConfig',
)


class CommentsAppConfig(AppConfig):
    """Configuration for Comments app."""
    name = 'apps.comments'
    verbose_name = "Comments"
