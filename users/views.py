from users.forms import UserForm
from django.http import HttpResponseRedirect
from users.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("home")

    def post(self, request):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)

        else:
            return self.form_invalid(form)


class UserSignupView(CreateView):
    template_name = "users/signup.html"
    model = User
    form_class = UserForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UserLogoutView(LogoutView):
    template_name = "core/index.html"
