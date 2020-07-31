from django import forms

from .models import Review

__all__ = (
    'ReviewForm',
)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            'title',
            'text',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'type':'search'}),
        }
