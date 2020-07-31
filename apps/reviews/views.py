from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Review
from .forms import ReviewForm

__all__ = (
    'ReviewIndex',
    'ReviewCreate',
)


class ReviewIndex(ListView):
    model = Review
    template_name = 'reviews/list.html'
    context_object_name = 'reviews'


class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews:index')

    def form_valid(self, form):
        # set current user to the created Review
        form.instance.author = self.request.user
        return super().form_valid(form)
