import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_square.settings')

app = Celery('stock_square')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {

    #       ----------------------------------- NEWS SCRIPT --------------------------------------

    # # executes every 1 hour --> 1
    # 'scraping-IPONews-task-every-one-hour': {
    #     'task': 'stock_square_api.task.IPO.IPONewsMethod',
    #     'schedule': crontab(minute='*/5'),
    # },
    # executes every 1 hour --> 2
    'scraping-MoneyControlNews-task-every-one-hour': {
        'task': 'stock_square_api.task.moneycontrol.MoneyControlNewsMethod',
        'schedule': crontab(minute='*/5'),
    },
    # # executes every 1 hour --> 3
    # 'scraping-newsScripts-task-every-one-hour': {
    #     'task': 'stock_square_api.task.newsScripts.NewsScriptsMethod',
    #     'schedule': crontab(minute='*/10'),
    # },


}
