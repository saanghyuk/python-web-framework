from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class RegisterForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': "Please Enter the Email"
    }, max_length=64, label="EMAIL")
    password = forms.CharField(error_messages={
        'required': "Please Enter the Password"
    }, widget=forms.PasswordInput, label="PASSWORD")

    re_password = forms.CharField(error_messages={
        'required': "Please Re-Enter the Password"
    }, widget=forms.PasswordInput, label="PASSWORD CHECK")

    def clean(self):
        # 기존 기본 유효성 검사를 먼저 호출
        cleaned_data = super().clean()
        email=cleaned_data['email']
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', "Two Password Different To Each Other")
                self.add_error('re_password', "Two Password Different To Each Other")
            else:
                try:
                    user = User.objects.get(email=email)
                    self.add_error('email', "Email Already Registered")
                except User.DoesNotExist:

                    return



class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': "Please Enter the Email"
    }, max_length=64, label="EMAIL")
    password = forms.CharField(error_messages={
        'required': "Please Enter the Password"
    }, widget=forms.PasswordInput, label="PASSWORD")

    def clean(self):
        cleaned_data = super().clean()
        email=cleaned_data['email']
        password = cleaned_data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            self.add_error('email', "There's No User with this Email")
            return
        if not check_password(password, user.password):
            self.add_error('password', "Wrong Password")
        else:
            self.email = user.email