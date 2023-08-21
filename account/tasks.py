from account.models import OTP
from celery import shared_task
from datetime import datetime, timedelta
import pytz

@shared_task
def remove_expire_otp_codes():
    expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    OTP.objects.filter(create_time__lt=expired_time).delete()