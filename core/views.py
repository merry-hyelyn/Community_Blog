from boards.models import Board
from posts.models import Post
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


class IndexView(TemplateView):
    template_name = "core/index.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_list'] = Board.objects.all()

        path = kwargs.get('path', '')
        posts_list = Post.objects.filter(board__path=path)
        pagination = Paginator(posts_list, 6)
        context['pagination'] = pagination

        page = self.request.GET.get('page')
        posts = pagination.get_page(page)
        context['post_list'] = posts
        return context


class BoardDelete(DeleteView):
    model = Board
    success_url = reverse_lazy("home")

    def get_object(self):
        return get_object_or_404(Board, pk=self.kwargs.get("pk"))
