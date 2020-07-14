from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from users.forms import UserForm
from django.http import HttpResponse
from users.models import User


# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_user.save()
        return redirect("login")

    else:
        user_form = UserForm()
        return render(request, "users/signup.html", {"user_form": user_form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pwd"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
        else:
            messages.add_message(request, messages.ERROR,
                                 "Username or password is incorrect.")

        return redirect(reverse("index"))
    else:
        return render(request, "core/index.html")


def logout(request):
    auth.logout(request)
    return redirect(reverse("index"))
