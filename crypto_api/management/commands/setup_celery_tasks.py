from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask,IntervalSchedule,CrontabSchedule
import json

class Command(BaseCommand):
    help = "Setup periodic Celery tasks in Django celery beats"
    def handle(self,*args,**kwargs):
        schedule,created = CrontabSchedule.objects.get_or_create(
            minute="*/5",hour="*",day_of_week="*",day_of_month="*",month_of_year="*"
        )
        task,created = PeriodicTask.objects.get_or_create(
            crontab=schedule,
            name="Updating crypto prices every 5 minutes by cronjab",
            task='crypto_api.tasks.update_crypto_prices',
            defaults={"args":json.dumps([])}
        )

        if created:
            self.stdout.write(self.style.SUCCESS("Successfully created periodic task"))
        else:
            self.stdout.write(self.style.WARNING("Task already exists"))