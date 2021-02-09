from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    return x+y

@shared_task
def sleepy(duration):
    sleep(duration)
    print("Wake up wake up")
    return None