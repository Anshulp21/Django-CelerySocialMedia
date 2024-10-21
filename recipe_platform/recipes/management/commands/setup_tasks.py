from django.core.management.base import BaseCommand
from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask
from recipes.tasks import export_users_to_csv, send_daily_email

class Command(BaseCommand):
    help = 'Set up scheduled tasks'

    def handle(self, *args, **kwargs):
        # Schedule a task to send daily emails at 6 AM
        email_schedule, email_created = CrontabSchedule.objects.get_or_create(
            hour=6, minute=0  # 6 AM schedule
        )

        # Create the periodic task for sending daily email at 6 AM
        email_task, email_task_created = PeriodicTask.objects.get_or_create(
            crontab=email_schedule,  # Use the crontab schedule for daily tasks
            name='Send daily email at 6 AM',
            task='recipes.tasks.send_daily_email',
        )

        # Set up interval for exporting users to CSV every 20 seconds
        csv_schedule, csv_created = IntervalSchedule.objects.get_or_create(
            every=20,
            period=IntervalSchedule.SECONDS  # Interval in seconds
        )

        # Create the periodic task for exporting users to CSV every 20 seconds
        csv_task, csv_task_created = PeriodicTask.objects.get_or_create(
            interval=csv_schedule,  # Use the interval schedule
            name='Export users to CSV every 20 seconds',
            task='recipes.tasks.export_users_to_csv',
        )
        # Print success message only if tasks were created
        if csv_task_created or email_task_created:
            self.stdout.write(self.style.SUCCESS('Successfully set up tasks for sending emails at 6 AM and exporting users every 20 seconds'))
        else:
            self.stdout.write(self.style.WARNING('Tasks are already set up'))





# from django.core.management.base import BaseCommand
# from django_celery_beat.models import CrontabSchedule, IntervalSchedule, PeriodicTask
# from recipes.tasks import export_users_to_csv, send_daily_email

# class Command(BaseCommand):
#     help = 'Set up scheduled tasks'

#     def handle(self, *args, **kwargs):
#         # Schedule for exporting users to CSV at 2 AM daily
#         csv_schedule, csv_created = CrontabSchedule.objects.get_or_create(
#             hour=2, minute=35  # Schedule at 2:35 AM
#         )
#         # Create or get the periodic task for exporting users
#         csv_task, csv_task_created = PeriodicTask.objects.get_or_create(
#             crontab=csv_schedule,
#             name='Export users to CSV',  # Name of the task
#             defaults={'task': 'recipes.tasks.export_users_to_csv'}  # Task function to run
#         )

#         # Set up interval for sending email every 20 seconds
#         email_schedule, email_created = IntervalSchedule.objects.get_or_create(
#             every=20,
#             period=IntervalSchedule.SECONDS  # Interval in seconds
#         )

#         # Create the periodic task for sending daily email
#         email_task, email_task_created = PeriodicTask.objects.get_or_create(
#             interval=email_schedule,  # Use the interval schedule
#             name='Send daily email every 20 seconds',
#             task='recipes.tasks.send_daily_email',
#         )

#         # Print success message only if tasks were created
#         if csv_task_created or email_task_created:
#             self.stdout.write(self.style.SUCCESS('Successfully set up tasks for exporting users and sending emails'))
#         else:
#             self.stdout.write(self.style.WARNING('Tasks are already set up'))
