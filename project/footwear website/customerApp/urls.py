from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = "home"),
    path("contact/", contact, name = "contact"),
    path("signup/", signup, name ="signup"),
    path("signin/", signin, name ="signin"),
    path("signout/", signout, name ="signout"),
    path("profile/", profile, name ="profile"),
    path("change_password/", change_password, name ="change_password"),
]
