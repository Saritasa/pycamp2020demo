from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from django_object_actions import DjangoObjectActions

from apps.reviews.admin import ReadonlyReviewInline
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User

__all__ = (
    'UserAdmin',
)

def deactivate(modeladmin, request, queryset):
    """Deactivate all users except superuser."""
    qs = queryset.exclude(is_superuser=True)
    qs.update(is_active=False)

    # show message
    messages.success(request, f"Deactivated {qs.count()} user(s)")


@admin.register(User)
class UserAdmin(DjangoObjectActions, DjangoUserAdmin):
    """User admin.

    Admin class definitions for ``User`` model.

    """
    search_fields = ('first_name', 'last_name', 'email')
    list_display = (
        'id',
        'email',
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    list_display_links = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name',
                'last_name',
            )
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
        (_('Permissions'), {
            'classes': (
                'collapse',
            ),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = DjangoUserAdmin.readonly_fields + (
        'last_login',
        'date_joined',
    )
    ordering = ('email',)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    inlines = [ReadonlyReviewInline]
    actions = [deactivate]
    change_actions = ['deactivate']

    def deactivate(self, request, obj):

        if not obj.is_superuser:
            obj.is_active = False
            obj.save()

        # show message
        messages.success(request, f"User {obj.get_full_name()} deactivated")
