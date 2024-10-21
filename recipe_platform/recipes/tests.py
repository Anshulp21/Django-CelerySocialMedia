# # from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from .models import Recipe, Rating
# from django.contrib.auth.models import User

# class RecipeModelTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.recipe = Recipe.objects.create(seller=self.user, name='Test Recipe', description='Delicious!', image='../../picture.jpg')

#     def test_recipe_creation(self):
#         self.assertEqual(self.recipe.name, 'Test Recipe')
#         self.assertEqual(self.recipe.seller.username, 'testuser')


# python manage.py shell

# from django.core.mail import send_mail
#  send_mail('Test Email', 'This is a test', 'anshulpurohit96@gmail.com', ['anshulp490@gmail.com'], fail_silently=False)



# from django_celery_beat.models import PeriodicTask
# PeriodicTask.objects.filter(name='Export users to CSV').delete()