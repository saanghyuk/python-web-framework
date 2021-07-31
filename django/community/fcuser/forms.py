from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        "required": "Enter the username please"
    },
        max_length=32, label="User Name")
    password = forms.CharField(error_messages={
        "required": "Enter the password please"
    }, widget=forms.PasswordInput, label="Password")

    # 기존에 정의되있는 함수
    # 이것을 다 만족해야, is_valid에서 True가 나오는 것.
    # Default로 모든 칸 채우기는 됨(그게 super())
    def clean(self):

        # 기존 기본 유효성 검사를 먼저 호출
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
                if not check_password(password, fcuser.password):
                    # 특정 필드에 에러를 넣는 함수
                    self.add_error('password', "Wrong Password")
                else:
                    self.user_id = fcuser.id

            except:
                self.add_error('username', "No USERNAME IN DB")
