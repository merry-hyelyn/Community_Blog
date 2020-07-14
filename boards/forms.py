from django import forms
from boards.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = [
            'create_user',
        ]

        field = [
            "name",
            "path",
        ]

        widgets = {
            "path":
            forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "위와 동일한 이름 권장",
            }),
        }
