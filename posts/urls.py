from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from . import views

manage_permission = user_passes_test(lambda u: u.is_staff or u.is_superuser,
                                     login_url='index')
urlpatterns = [
    path('new_post/', views.CreatePost.as_view(), name="new_post"),
    path('delete_post/<int:post_id>/',
         manage_permission(views.DeletePost.as_view()),
         name="delete_post"),
    path('detail_post/<int:post_id>/',
         views.DetailPost.as_view(),
         name="detail_post"),
    path('update_post/<int:post_id>/',
         views.UpdatePost.as_view(),
         name="update_post")
]
