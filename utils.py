# from kavenegar import *
from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin

def send_otp_code(phone_number,code):
    # api = KavenegarAPI('505333704638615A5234325A6B63316B573071396F41435446306E3358654E7668506562664366416667673D')
    # params = { 'sender' : '', 'receptor': phone_number, 'message' :f'{code} کد شما:'}
    # response = api.sms_send( params)
    # print('-'*98)
    # print(response)
    pass

class IsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
        