import os

from celery import Celery
# from core.tasks import test_celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# run test_celery in every 10 seconds
# app.conf.beat_schedule = {
#     'test-celery-every-10-seconds': {
#         'task': 'core.tasks.test_celery',
#         'schedule': 10.0,
#     },
# }