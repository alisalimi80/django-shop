from bucket import bucket
from celery import shared_task

@shared_task
def delete_object(key):
    bucket.delete_object(key)
    

@shared_task
def download_object(key):
    bucket.download_object(key)