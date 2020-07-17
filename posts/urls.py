from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
manage_permission = user_passes_test(lambda u: u.is_staff or u.is_superuser,
                                     login_url='index')
urlpatterns = [
    path('new_post/', csrf_exempt(views.CreatePost.as_view()),
         name="new_post"),
    path('delete_post/<int:pk>/',
         manage_permission(views.DeletePost.as_view()),
         name="delete_post"),
    path('detail_post/<int:pk>/',
         views.DetailPost.as_view(),
         name="detail_post"),
    path('update_post/<int:pk>/',
         views.UpdatePost.as_view(),
         name="update_post"),
    path('download/<int:pk>/',
         views.FileDownloadView.as_view(),
         name="download"),
]
