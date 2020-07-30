from django.contrib import admin

from .models import Comment

__all__ = (
    'CommentInlineAdmin',
)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'author',
        'date_created',
    ]


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    fields = [
        'author',
        'text',
        'date_created',
    ]
    readonly_fields = [
        'date_created',
    ]
    extra = 0
    raw_id_fields = [
        'author',
    ]
