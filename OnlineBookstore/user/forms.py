from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class registry(UserCreationForm):
    姓名 = forms.CharField(required=True, max_length=15)
    昵称 = forms.CharField(required=True, max_length=15)
    手机号 = forms.CharField(required=True, max_length=11)

    class Meta:
        model=User
        fields=('username','password1','password2','姓名','昵称','手机号')

class edit(UserChangeForm):
    姓名 = forms.CharField(required=True, max_length=15)
    昵称 = forms.CharField(required=True, max_length=15)
    手机号 = forms.CharField(required=True, max_length=11)

    class Meta:
        model=User
        fields=('username','password','姓名','昵称','手机号')