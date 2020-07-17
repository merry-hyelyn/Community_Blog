from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('signup/', views.UserSignupView.as_view(), name="signup"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
]