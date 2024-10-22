
from django.apps import AppConfig

class RecipesConfig(AppConfig):
    name = 'recipes'

    def ready(self):
        # No database queries here
        pass





