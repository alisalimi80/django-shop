from django.shortcuts import render , redirect
from django.views import View
import random
from .models import OTP , User
from .utils import send_otp_code
from .forms import UserRegisterForm , VerifyCodeForm
from django.contrib import messages

# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'account/register.html'
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_number = random.randint(1000,999999)
            send_otp_code(form.cleaned_data['phone_number'],random_number)
            OTP.objects.create(phone_number=form.cleaned_data['phone_number'],code=random_number)
            request.session['user_register_info'] = {
                'phone_number' : form.cleaned_data['phone_number'],
                'email' : form.cleaned_data['email'],
                'full_name' : form.cleaned_data['full_name'],
                'password' : form.cleaned_data['password']
            }
            messages.success(request,'we sent some code to your phone','success')
            return redirect('account:verify_code')
        return render(request,self.template_name,{'form':form})

class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self,request):
        form = self.form_class
        return render(request,'account/verify.html',{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            session_data = request.session['user_register_info']
            phone_number = session_data['phone_number']
            otp_instance = OTP.objects.get(phone_number=phone_number)
            database_otp_code = otp_instance.code
            if database_otp_code and database_otp_code == cd['verify_code']:
                otp_instance.delete()
                User.objects.create_user(session_data['email'],session_data['phone_number'],
                                         session_data['full_name'],session_data['password'])
                messages.success(request,'your account registered','success')
                return redirect('home:home')
            messages.error(request,'this code is wrong','danger')
            return redirect('account:verify_code')
        return redirect('home:home')




            