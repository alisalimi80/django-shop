from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'account'

urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='user-register')
]