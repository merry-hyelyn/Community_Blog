from boards.models import Board
from posts.models import Post
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_list'] = Board.objects.all()
        path = ""

        for v in kwargs.values():
            path = v

        posts = Post.objects.filter(board__path=path)
        context['post_list'] = posts
        return context
