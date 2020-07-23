from boards.forms import BoardForm
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class CreateBoard(CreateView):
    form_class = BoardForm
    template_name = "boards/new.html"
    success_url = reverse_lazy("index")

    # method == POST 일 때 실행
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.create_user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())