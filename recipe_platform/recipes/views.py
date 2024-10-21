from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Recipe, Rating
from .serializers import RecipeSerializer, RatingSerializer
from .tasks import resize_image  # Import the resize task

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.select_related('seller').all()  # Optimize querying related user
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        recipe = serializer.save()
        # Call the resize image task asynchronously after saving the recipe
        resize_image.delay(recipe.image.path)

class RatingCreateView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

# k