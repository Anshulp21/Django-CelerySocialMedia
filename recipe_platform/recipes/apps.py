
# from django.apps import AppConfig

# class RecipesConfig(AppConfig):
#     name = 'recipes'

#     def ready(self):
#         # No database queries here
#         pass




from django.apps import AppConfig
from django.core.management import call_command

class RecipesConfig(AppConfig):
    name = 'recipes'

    def ready(self):
        # Automatically run setup_tasks when the server starts
        try:
            call_command('setup_tasks')
        except Exception as e:
            # Handle any errors, you can log this or print the error
            print(f"Error running setup_tasks: {e}")

