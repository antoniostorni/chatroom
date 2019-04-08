import os
from celery import Celery, Task
from django.apps import apps, AppConfig
from django.conf import settings
import requests
import csv


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "config.settings.local"
    )  # pragma: no cover


app = Celery("chatroom")
# Using a string here means the worker will not have to
# pickle the object when using Windows.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")


class CeleryAppConfig(AppConfig):
    name = "chatroom.taskapp"
    verbose_name = "Celery Config"

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")  # pragma: no cover


@app.task(name="get_stock", bind=True, default_retry_delay=0.1)
def get_stock(self, stock_name, user, room):
    from chatroom.chat.models import Message
    from chatroom.chat.models import Room
    from django.contrib.auth import get_user_model
    User = get_user_model()

    #req = requests.get("https://stooq.com/q/l/?s={stock}&f=sd2t2ohlcv&h&e=csv")
    url = f"https://stooq.com/q/l/?s={stock_name}&f=sd2t2ohlcv&h&e=csv"
    req = requests.get(url)

    decoded_content = req.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')

    csv_list = list(cr)

    price = csv_list[1][5]

    new_message = Message()
    new_message.content = f"BOT: {stock_name} quote is ${price} per share"
    new_message.user = User.objects.get(id=user)
    new_message.room = Room.objects.get(id=room)

    new_message.save()

    return 'OK'
