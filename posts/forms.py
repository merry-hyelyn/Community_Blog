from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            'user',
        ]

        # field = [
        #     "title",
        #     "content",
        #     "board",
        #     "secret",
        #     "file",
        # ]

        label = {
            "title": "제목",
            "content": "내용",
            "board": "게시판",
            "secret": "비밀글",
            "file": "파일"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False
