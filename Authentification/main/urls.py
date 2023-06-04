from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginPage, name = "LoginPage"),
    path("register/", views.RegisterPage, name = "RegisterPage"),
    path("welcome/", views.WelcomePage, name = "WelcomePage"),
    path("logout/",views.Logoutpage, name="LogoutPage")
] 