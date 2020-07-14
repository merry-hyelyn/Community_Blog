from django.contrib.auth.decorators import user_passes_test
from boards.forms import BoardForm
from django.views.generic import CreateView


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url="index")
class CreateBoard(CreateView):
    form_class = BoardForm
    template_name = "boards/new.html"
    success_url = "../../index"

    # method == POST 일 때 실행
    def form_valid(self, form):
        print(self.request.user)
        form.instance.create_user = self.request.user
        return super(CreateBoard, self).form_valid(form)