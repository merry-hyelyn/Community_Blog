from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from . import views

manage_permission = user_passes_test(lambda u: u.is_staff or u.is_superuser,
                                     login_url="index")
urlpatterns = [
    path("create/",
         manage_permission(views.CreateBoard.as_view()),
         name="create"),
]
