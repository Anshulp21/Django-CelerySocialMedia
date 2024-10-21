from django.urls import path
from .views import RecipeListCreateView, RatingCreateView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('rate/', RatingCreateView.as_view(), name='rate-recipe'),
]
