from django.urls import path
from . import views

urlpatterns = [
    path('new_post/', views.new_post, name="new_post"),
    path('detail_post/<int:post_id>/', views.detail_post, name="detail_post"),
    path('detail_post/<int:post_id>/', views.detail_post, name="detail_post"),
    path('update/<int:post_id>/', views.update, name="update"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
]
