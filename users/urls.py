from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.Register_Users, name="Register_Users"),
    path("login/", views.LogIn_Users, name="LogIn_Users"),
    path("viewUser", views.view_user, name="view_user"),
    path("logout", views.LogOut_Users, name="LogOut_Users"),
]
