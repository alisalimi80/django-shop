from typing import Any
from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,label='password')
    password2 = forms.CharField(widget=forms.PasswordInput,label='confirm password')

    class Meta:
        model = User
        fields = ('email','full_name','phone_number')

    def clean_password2(self):
        cd  = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            ValidationError('passwords does not match')
        return cd['password2']
    
    def save(self, commit:True):
        cd = self.cleaned_data
        user = super().save(commit=False)
        user.set_password(cd['password2'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you cant change password using <a href="../passwrod/"> this form </a>')
    class Meta:
        model = User
        fields = ('email','phone_number','last_login','password','full_name')

class UserRegisterForm(forms.Form):
    phone_number  = forms.CharField(max_length=11)
    email = forms.EmailField()
    full_name = forms.CharField(label='full name')
    password = forms.CharField(widget=forms.PasswordInput)



