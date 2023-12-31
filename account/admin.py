from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import Group
from .models import User,OTP


@admin.register(OTP)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number','code','create_time')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email','phone_number','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('email','full_name','phone_number','password')}),
        ('permissions',{'fields':('is_active','is_admin')})
    )
    add_fieldsets = (
        (None,{'fields':('email','phone_number','full_name','password1','password2')}),
    )

    search_fields = ('full_name','email','phone_number')
    ordering = ('full_name',)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)

