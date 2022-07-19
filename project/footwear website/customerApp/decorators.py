from django.shortcuts import render, redirect
from .models import *

def session_checker(view_func):
    def inner(request, *args, **context):
        try:
            if"email" in request.session:
                customer = Customer.objects.get(email = request.session["email"])
                context ["customer"] = customer
                return view_func(request, *args, **context)
            else:
                return redirect("signin")
        except:
            return view_func(request, *args, **context)
    return inner