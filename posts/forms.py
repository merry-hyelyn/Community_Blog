from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            'user',
        ]

        field = [
            "title",
            "content",
            "board",
            "secret",
        ]

        label = {
            "title": "제목",
            "content": "내용",
            "board": "게시판",
            "secret": "비밀글",
        }
