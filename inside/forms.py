from django import forms
from inside.models import User
from .models import UserProfileInfo
from django.contrib.auth.models import User as UserAdmin

class FormRegister(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = UserAdmin
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    picture = forms.ImageField(required = False)
    class Meta():
        model = UserProfileInfo
        exclude = ('user', )
