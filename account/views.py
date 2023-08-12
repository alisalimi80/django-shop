from django.shortcuts import render
from django.views import View
from .forms import UserRegisterForm

# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self,request):
        form = self.form_class
        return render(request,'account/register.html',{'form':form})
    
    def post(self,request):
        pass