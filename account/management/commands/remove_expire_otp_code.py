from django.core.management.base import BaseCommand
from account.models import OTP
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
	help = 'remove all expired otp codes'

	def handle(self, *args, **options):
		expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
		OTP.objects.filter(create_time__lt=expired_time).delete()
		self.stdout.write('all expired otp codes removed.')