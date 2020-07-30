from django.contrib import admin

from apps.comments.admin import CommentInlineAdmin
from apps.reviews.models import Review
from .models import Review

__all__ = (
    'ReadonlyReviewInline',
)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines = [CommentInlineAdmin]
    search_fields = [
        'text',
        'title',
        'author__email',
    ]
    list_display = [
        'id',
        'title',
        'author',
        'date_created',
        'is_published',
    ]
    list_select_related = [
        'author',
    ]
    raw_id_fields = [
        'author',
    ]


class ReadonlyReviewInline(admin.StackedInline):
    model = Review
    fields = [
        'title',
        'text',
        'date_created'
    ]
    readonly_fields = fields
    extra = 0
    can_delete = False
    add_another = False
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        return False
