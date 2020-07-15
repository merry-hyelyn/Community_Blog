from django.shortcuts import get_object_or_404
from posts.forms import PostForm
from posts.models import Post
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
# Create your views here.


class CreatePost(CreateView):
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = "../../index"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class DetailPost(DetailView):
    model = Post
    template_name = "posts/detail_post.html"
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"
    context_object_name = "post"
    success_url = "../../../index"

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))

    def form_valid(self, form):
        return super(UpdatePost, self).form_valid(form)


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("index")

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_id"))