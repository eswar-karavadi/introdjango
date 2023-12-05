from django.urls import path
from reviews.views import AppDevClubReviewsView, AppDevClubReviewsAdd

urlpatterns = [
    path('reviews', AppDevClubReviewsView.as_view()),
    path('reviews', AppDevClubReviewsAdd.as_view())
]
