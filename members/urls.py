from django.urls import path, include
from members.views import register_user, login_user, logout_user

urlpatterns = [
    path("", login_user, name="root"),
    path("register/", register_user, name="register-user"),
    path("login/", login_user, name="login-user"),
    path("logout/", logout_user, name="logout-user"),
]
