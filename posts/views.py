from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import user_passes_test
from posts.forms import PostForm
from posts.models import Post

# Create your views here.


def new_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        post_form = PostForm()
        return render(request, 'posts/new_post.html', {
            'post_form': post_form,
            'user': request.user,
        })


def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.secret == "true":
        if post.user == request.user or request.user.is_staff or request.user.is_superuser:
            return render(request, 'posts/detail_post.html', {'post': post})

        else:
            return redirect(reverse("index"))
    else:
        return render(request, 'posts/detail_post.html', {'post': post})


def update(request, post_id):
    re_url = 'posts/detail_post/' + str(post_id)
    post = get_object_or_404(Post, pk=post_id)
    post_form = PostForm(request.POST, instance=post)
    if request.method == "POST":
        if post_form.is_valid():
            post_form.save()
            return redirect('/' + re_url)
    else:
        return render(request, 'posts/update_post.html', {
            'post_form': post_form,
            'post': post
        })


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='index')
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('index')