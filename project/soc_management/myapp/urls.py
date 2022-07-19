from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name ="home"),
    path("login/", login, name ="login"),
    path("register/", register, name ="register"),
    path("profile/", profile, name ="profile"),
    path("logout/", logout, name ="logout"),
    path("changepassword/", change_password, name ="change_password"),
    path("editprofile/", editprofile, name ="edit_profile"),
    path("notfound/", notfound, name ="notfound"),
    path("add-member/", add_member, name ="add_member"),
    path("all-member/", all_member, name = "all_member"),
    path("add_notice/", add_notice, name = "add_notice"),
    path("all_notice/", all_notice, name = "all_notice"),
    path("add_event/", add_event, name = "add_event"),
    path("all_event/", all_event, name = "all_event"),
    path("mem_profile/", mem_profile, name = "mem_profile"),
    path("mem_edit_profile/", mem_edit_profile, name = "mem_edit_profile"),
    path("mem_all_notice/", mem_all_notice, name = "mem_all_notice"),
    path("mem_all_member/", mem_all_member, name = "mem_all_member"),
    path("mem_all_event/", mem_all_event, name = "mem_all_event"),
    
]
