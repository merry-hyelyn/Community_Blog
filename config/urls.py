"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

manage_permission = user_passes_test(lambda u: u.is_staff or u.is_superuser,
                                     login_url='home')
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="home"),
    path("<int:pk>",
         manage_permission(views.BoardDelete.as_view()),
         name="delete"),
    path("index/<str:path>", views.IndexView.as_view(), name="index"),
    path("users/", include("users.urls")),
    path("boards/", include("boards.urls")),
    path("posts/", include("posts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
