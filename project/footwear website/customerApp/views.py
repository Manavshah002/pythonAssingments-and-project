from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from .decorators import session_checker
from uuid import uuid4


# Create your views here.
def index(request):
    return render(request, "index.html")

@session_checker
def contact(request, *args, **context):
    if request.method == 'POST':
        try:
                user  = Contact.objects.create(
                    fname = request.POST["fname"],
                    lname = request.POST["lname"],
                    email = request.POST["email"],
                    subject = request.POST["subject"],
                    message = request.POST["message"]   
                )
                user.save()
                
                # sender
                subject = f" Message received from {user.email}"
                message = f"Subject : {user.email} \nMessage : {user.message}" 
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [settings.EMAIL_HOST_USER, ]
                send_mail( subject, message, email_from, recipient_list )

                # receiver
                subject = f'Contact request sent successfully'
                message = f'Hello {user.fname},\nHope this message finds you well.\n\nYour message has been received successfully and our team with get back in touch with you asap.\n\nBest regards,\tTeam Nakami Website.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail( subject, message, email_from, recipient_list )

                context.update ({
                    "msg_s" : "Message sent successfully..."
                })
                return render(request, "contact.html", context=context)
        except Exception as e:
            print(f"\n\n\n{e}\n\n\n")       
            context.update ({
                "msg_d" : "Something went wrong..."
                })
            return render(request, "contact.html", context=context)
        
    else:   
        return render(request, "contact.html")
    
def student_email_registration(request):
    if request.POST == "POST":
        try:
            customer.objects.get(email= request.POST["email"])
            context = {
                "msg_d" : "Email already registered..."
            }
            return render(request, "student_email_registration.html", context=context)
        except:
            token = str(uuid())[:6]
            email = request.POST["email"]
            verify_customer = Authenticate.objects.create(
                email= email,
                auth_token = token
            )
            subject = f"Email Registration | DO NOT REPLY"
            message = f"your secret OTP is: {token}"
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email,]
            send_mail(subject, message, email_from, recipient_list )
            context = {
                "email" : email,
            }
            return render(request, "student_otp_page.html", context=context)
    else:
        return render(request,"student_email_registration.html")
    
    
def signup(request):
    if request.method == "POST" :
        if request.POST["fname"] == "" or request.POST["lname"] == "" or request.POST["email"] == "" or request.POST['phone'] == "" or request.POST["password"] == '':
            context = {
                "msg_d" : "All Fields are Mandatory..."
            }
            return render(request, "signup.html", context=context)
        elif request.POST["password"] ==request.POST["c_password"]:
            customer = Customer.objects.create(
                fname = request.POST["fname"],
                lname = request.POST["lname"],
                email = request.POST["email"],
                phone = request.POST["phone"],
                address = request.POST["address"],
                password = request.POST["password"],
            )
            customer.save()
            context = {
                "msg_s" : "Account Created Successfully..."
            }
            return render(request, "signup.html", context=context)
        else:
            context = {
                "msg_d" : "Password and confirm password not matched..."
            }
    else:
        return render(request, "signup.html")
    
def signin(request):
    try:
        if request.method == "POST":
            if  request.POST["email"] == "" or request.POST["password"] == "":
                context ={
                    "msg_d" : "Please enter email and password to signin..."
                }
                return render(request, "signin.html", context=context)
            else:
                email_id = request.POST["email"]
                try: 
                    customer = Customer.objects.get(email=request.POST["email"], password= request.POST["password"])
                    request.session["email"] = customer.email
                    return redirect("home")
                except Exception as e:
                    print(f"\n\n\n{e}\n\n\n")
                    try:
                        customer = Customer.objects.get(email = request.POST["email"])
                        context = {
                            "msg_d" : "Invalid password",
                            "email_id" : email_id,
                        }
                        return render(request, "signin.html", context=context)
                    except:
                        context = {
                            "msg_d" : "u dont register in our site yet...",
                            "email_id" : email_id
                        }
                        return render(request, "signin.html", context=context)
        else:
            return render(request, "signin.html")
    except Exception as e:
        print(f"\n\n\n{e}\n\n\n")    
        
def signout(request):
    try:
        del request.session["email"]
        return redirect("signin")
    except:
        context = {
            "msg_d" : "signout was unsuccesful...", 
        }
        return render(request, "contact.html", context=context)

@session_checker
def profile(request, *args, **context):
    # if user already signup
    try:
        if request.method == "POST":
            # if user has not entered anything in columns
            if request.POST["fname"] == "" or request.POST["lname"] == "":
                context.update ({
                    "msd_d" : "Please enter the fname and lname..."
                })
                return render(request,"profile.html", context=context)
            # if all the fields are filled
            else:
                try:
                    
                    # the fields those who get updated in profile
                    context["customer"].fname = request.POST["fname"]
                    context["customer"].lname = request.POST["lname"]
                    context["customer"].address = request.POST["address"]
                    context.update ({
                        "msg_s" : "Profile updated successfully...",
                    })
                        
                    return render(request, "profile.html", context=context)
                except Exception as e:
                    print("\n\n\n{e}\n\n\n")
                    context.update ({
                        "msg_d": "Something went wrong...",
                        
                    })
                    return render(request, "profile.html", context=context)
        else:
            return render(request, "profile.html", context=context)
        
            # if user has not signup atleast once    
    except Exception as e:
            print("\n\n\n{e}\n\n\n")
            context.update ({
                "msg_d" : "Please log in to view your profile.."
            })
            return render(request, "signin.html", context=context)

@session_checker    
def change_password(request, *args, **context):
    try:
        if request.POST == "POST":
                if request.POST["old_password"] == "" or request.POST["new_password"] == "" or request.POST["confirm_password"] == "":
                    context.update ({
                        "msg_d" : "All fields are mandatory..."
                        })
                    return render(request, "change_password.html", context=context)   
                
                elif request.POST["old_password"] == context["customer"].password :
                    if request.POST["new_password"] != request.POST["old_password"]:
                        if request.POST["new_password"] == request.POST["confirm_password"]:
                            try:
                                context["customer"].password = request.POST["new_password"]
                                context["customer"].save()
                                context.update ({
                                    "msg_s" : "password changed successfully..."
                                })
                                return render(request, "change_password.html", context=context)
                            
                            except Exception as e:
                                context.update ({
                                    "msg_d" : "Something went wrong..."
                                })
                                return render(request, "change_password.html", context=context)
                        else:
                            context.update ({
                                "msg_d" : "New password and confirm password doesnt match..."
                            })
                            return render(request, "change_password.html", context=context)
                    else:
                        context.update({
                            "msg_d" : "Your new password is same as old password..."
                        })
                        return render(request, "change_password.html", context=context)
                        
                else:
                    context.update({
                        "msg_d" : "Your old password is wrong..."
                    })
                    return render(request, "change_password.html", context = context)
        else:
            return render(request, "change_password.html", context=context)
        
    except Exception as e:
        print(f"\n\n\n{e}\n\n\n")
        context.update ({
            "msg_d" : "Something went wrong..."
        })
        return render(request, "change_password.html", context=context)
        
