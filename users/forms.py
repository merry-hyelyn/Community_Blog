from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
        ]

        widgets = {
            "username":
            forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "15자 이내로 입력"
            }),
            "email":
            forms.EmailInput(attrs={"class": "form-control"}),
            "password":
            forms.PasswordInput(attrs={"class": "form-control"}),
        }

        label = {
            "username": "이름",
            "email": "이메일",
            "password": "비밀번호",
        }
