from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from posts.forms import PostForm
from posts.models import Post
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, View
from django.urls import reverse_lazy


class CreatePost(CreateView):
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("home")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        print(self.request.FILES)
        print(form)

        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.file = self.request.FILES['file']
            self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class DetailPost(DetailView):
    model = Post
    template_name = "posts/detail_post.html"
    context_object_name = 'post'

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("pk"))


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"
    context_object_name = "post"

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("pk"))

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        redirect_url = reverse_lazy('detail_post',
                                    kwargs={'pk': self.object.pk})
        return redirect_url


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("home")

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get("pk"))


class FileDownloadView(View):
    pass