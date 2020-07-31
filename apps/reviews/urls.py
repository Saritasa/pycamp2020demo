from django.urls import path
from apps.reviews.views import ReviewCreate, ReviewIndex

urlpatterns = [
    path('', ReviewIndex.as_view(), name='index'),
    path('create/', ReviewCreate.as_view(), name='create'),
]
