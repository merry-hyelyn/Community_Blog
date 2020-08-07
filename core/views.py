from boards.models import Board
from posts.models import Post
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class IndexView(TemplateView):
    template_name = "core/index.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_list'] = Board.objects.all()
        path = ""

        for v in kwargs.values():
            path = v

        posts = Post.objects.filter(board__path=path)
        path = kwargs.get('path', '')
        posts_list = Post.objects.filter(board__path=path)
        pagination = Paginator(posts_list, 6)
        page = self.request.GET.get('page')
        print('kwargs', kwargs, pagination)
        posts = pagination.get_page(page)
        context['post_list'] = posts
        return context
