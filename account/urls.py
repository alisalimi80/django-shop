from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'account'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='user-register'),
    path('register/verfication/',views.UserRegisterVerifyCodeView.as_view(),name='verify_code'),
    path('login/',views.UserLoginView.as_view(),name='user-login'),
    path('logout/',views.UserLogoutView.as_view(),name='user-logout'),
    
]