from cryptoapp.models import SubscribedUsers

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return SubscribedUsers.objects.count()


@shared_task
def rename_widget(widget_id, email):
    w = SubscribedUsers.objects.get(id=widget_id)
    w.email = email
    w.save()