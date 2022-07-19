from django.shortcuts import render, redirect
from .models import *
from uuid import uuid4

# Create your views here.


def index(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        print(request.session["email"])
        
        if u_id.role == "chairman":
            c_id = Chairman.objects.get(user_id = u_id)
            context = {
                "u_id" : u_id,
                "c_id" : c_id
            }
            return render(request, "myapps/index.html", context)
        else:
            m_id = Add_member.objects.get(m_user_id = u_id)
            context = {
                "u_id" : u_id,
                "m_id" : m_id
            }
            return render(request, "myapps/mem_index.html", context)
        
    else:
        return render(request, "myapps/login.html")
  
  
def login(request):
    if "email" in request.session :
        return redirect("home")
    
    else:
        if request.POST:
            v_email = request.POST["email"]
            v_password = request.POST["password"]
            try:
                u_id = User.objects.get(email = request.POST["email"])
                
                if u_id.password == v_password and u_id.role == "chairman":
                    c_id = Chairman.objects.get(user_id = u_id)
                    request.session["email"] = v_email
                    context = {
                        "u_id" : u_id,
                        "c_id" : c_id
                    }  
                    return render(request, "myapps/index.html", context)
                elif u_id.password == v_password and u_id.role == "member":
                    m_id = Add_member.objects.get(m_user_id = u_id)
                    request.session["email"] = v_email
                    context = {
                        "u_id" : u_id,
                        "m_id" : m_id
                    }
                    return render(request, "myapps/mem-index.html", context)
                else:
                    context = {
                        "msg" : "invalid password"
                    }
                    return render(request, "myapps/login.html", context)
            except Exception as e:
                print(f"\n\n\n{e}\n\n\n")
                context ={
                    "msg" : "invalid email"
                }   
                return render(request, "myapps/login.html", context)
        else:
            return render(request, "myapps/login.html", context)
        
def register(request):
    return httpResponse("<h1> register page </h1>")
        
def profile(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        
        if c_id:
            context ={
                "u_id" : u_id,
                "c_id" : c_id
            }
            return render(request, "myapps/profile.html", context)
        else:
            return render(request, "myapps/login.html")
    else:
        return render(request, "myapps/login.html")
    
def logout(request):
    if "email" in request.session:
        del request.session["email"]
        
        return render(request, "myapps/login.html")
    else:
        return render(request, "myapps/login.html")
    
def change_password(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        if request.POST:
            old_password = request.POST["password"]
            new_password = request.POST["newpassword"]
            confirm_password = request.POST["cpassword"]
            if old_password != new_password :
                if old_password == u_id.password:
                    if new_password == confirm_password:
                        u_id.password = new_password
                        u_id.save()
                        context = {
                            "smsg" : "Your pasword is successfully changed..."
                        }
                        return render(request, "myapps/profile.html")
                    else:
                        context = {
                            "emsg" : "confirm password and new password doesn't match", 
                            "c_id" : c_id  
                        }
                        return render(request, "myapps/profile.html", context)     
                else:
                    context = {
                        "emsg" : " old password is wrong", 
                        "c_id" : c_id  
                    }
                    return render(request, "myapps/profile.html", context)    
            else:
                context = {
                    "emsg" : "old password and new password is same", 
                    "c_id" : c_id  
                }
                return render(request, "myapps/profile.html", context) 
        else:
            context = {
                "emsg" : "something went wrong...",
                "c_id" : c_id
            }
            return render(request, "myapps/profile.html", context)
            

def editprofile(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        if request.POST:
            c_id = Chairman.objects.get(user_id = u_id)
            if c_id :
                c_id.firstname = request.POST['fname']
                c_id.lastname = request.POST['lname']
                c_id.contact = request.POST['contact']
                c_id.block_no = request.POST['blockno']
                c_id.house_no = request.POST['house_no']
                c_id.aboutme = request.POST['aboutme']
                
                if pic in request.FILES:
                    c_id.pic = request.POST["pic"]
                    
                c_id.save()
                context = {
                    "s_msg" : "u_id successfully updated...",
                    "c_id" : c_id,
                    "u_id" : u_id
                }
                return render (request, "myapps/profile.html",context)
            else:
                context = {
                    "e_msg" : "Error while updating u_id",
                    "c_id" : c_id
                }
                return render(request, "myapps/profile.html", context)

def mem_profile(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        
        m_id = Add_member.objects.get(m_user_id = u_id)
        context = {
            "m_id" : m_id,
            "u_id" : u_id
        }
        return render(request, "myapps/mem_profile.html", context)
    else:
        return render(request, "myapps/login.html")

def mem_change_password(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        context = {
            "u_id" : u_id,
            "c_id" : c_id
        }
        return render (request, "myapps/mem_profile.html", context)

        if request.POST:
            old_password = request.POST["old_password"]
            new_password = request.POST["new_password"]
            c_password = request.POST["c_password"]
            
            if old_password != new_password:
                if new_password == c_password:
                    if old_password == u_id.password:
                        u_id.password == new_password
                        u_id.save()
                        context = {
                            "s_msg" :"your password is successfully changed..."
                            
                        }
                        return render(request, "myapps/mem_profile.html", context)
                    else:
                        context = {
                            "e_msg" : 'invalid password...'
                         }
                        return render(request, "myapps/mem_profile.html", context)
                else:
                    return render(request, "myapps/mem_profile.html")
                
            else:
                return render(request, "myapps/mem_profile.html")


def mem_edit_profile(request):
    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        if request.POST:
            m_id = Add_member.objects.get(m_user_id = u_id)
            if m_id:
                m_id.m_f_name = request.POST["f_name"]
                m_id.m_l_name = request.POST["l_name"]
                m_id.dob = request.POST["dob"]
                m_id.gender = request.POST["gender"]
                m_id.vehicle = request.POST["vehicle"]
                m_id.work = request.POST["work"]
                m_id.m_block_no = request.POST["m_block_no"]
                m_id.m_house_no = request.POST["m_house_no"]
                m_id.family_member = request.POST["family_member"]
                m_id.contact_no = request.POST["contact"]
                m_id.m_about_me = request.POST["m_about_me"]
                
                m_id.save()
                
                if "m_pic" in request.FILES:
                    m_id.m_pic = request.FILES["m_pic"]
                    m_id.save()
                    
                    context = {
                        "s_msg" : "Profile successfully updated",
                        "m_id" : m_id,
                        "u_id" : u_id
                    }
                    return render(request, "myapps/mem_profile.html", context)
        else:
            context = {
                "e_msg" : "Something went wrong...",
                "m_id" : m_id
            }
            return render (request, "myapps/mem_profile", context)
    else:
        return render (request, "myapps/login.html")
        
               

def notfound(request):
    return render(request, "myapps/page404.html")

def add_member(request):
    
    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        context = {
            "u_id" : u_id,
            "c_id" : c_id
        }
        if request.POST:
            
            passwrd = str(uuid4())[:6]
            
            new_u_id = User.objects.create(
                email = request.POST["email"],
                password=  passwrd,
                role="member",
            ) 
            new_u_id.save()

            m_id = Add_member.objects.create(
                m_user_id= new_u_id,
                m_f_name = request.POST["f_name"],
                m_l_name = request.POST["l_name"],
                dob = request.POST["dob"],
                gender = request.POST["gender"],
                vehicle = request.POST["vehicle"],
                work = request.POST["work"],
                m_block_no = request.POST["block_no"],
                m_house_no = request.POST["house_no"],
                family_member = request.POST["family_member"],
                contact_no = request.POST["contact"],
                m_about_me = request.POST["about_me"],
            )
            m_id.save()
            context = {
                "u_id" : u_id,
                'c_id' : c_id,
                "m_id" : m_id
            }
            if "pic" in request.FILES:
                m_id.m_pic = request.FILES["pic"]
                m_id.save()
                
            if m_id : 
                context = {
                    "m_id" : m_id,
                    "c_id" : c_id,
                    "u_id" : u_id
                }
                return render(request, "myapps/add_member.html", context)
            else:
                return render(request, "myapps/add_member.html", context)
        
        else:
            return render(request, "myapps/add_member.html", context)
        
    else:
        return render(request, "myapps/login.html")
    
def all_member(request):
    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        m_id = Add_member.objects.all()
        context = {
            "c_id" : c_id,
            "u_id" : u_id,
            "m_id" : m_id
        }
        return render(request, "myapps/all_members.html", context)
    else:
        return render(request, "myapps/all_members.html")
    
def add_notice(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        context = {
            "c_id" : c_id,
            "u_id" : u_id
        }
        if request.POST:
            n_id = Add_notice.objects.create(
                user_id = c_id,
                title = request.POST["title"],
                content = request.POST["content"]
                )
            n_id.save()
            if "n_pic" in request.FILES:
                n_id.n_pic = request.FILES["n_pic"]
                n_id.save()
            
            if "n_video" in request.FILES:
                n_id.n_video = request.FILES["n_video"]
                n_id.save()
        
            return render(request, "myapps/add_notice.html", context)
        else:
            return render(request, "myapps/add_notice.html", context)
    else:
        return render(request, "myapps/login.html")
    
def all_notice(request):
    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        n_id = Add_notice.objects.all()
        context = {
            "u_id" : u_id,
            "c_id" : c_id,
            "n_id" : n_id
        }
        return render (request, "myapps/all_notice.html", context)
    else:
        return render(request, "myapps/all_notice.html", context)

def add_event(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        context = {
            "u_id" : u_id,
            "c_id" : c_id
        }
        if request.POST:
            e_id = Event.objects.create(
                user_id = c_id,
                e_title = request.POST["e_title"],
                e_content = request.POST["e_content"],
                e_venue = request.POST["e_venue"],
                e_date = request.POST["e_date"]
            )
            e_id.save()
            if "e_pic" in request.FILES:
                e_id.e_pic = request.FILES["e_pic"]
                e_id.save()
            return render(request, "myapps/add_event.html", context)
        
        else:
            return render(request, "myapps/add_event.html", context)
        
    else:
        return render(request, "myapps/login.html", context)
    
def all_event(request):
    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        c_id = Chairman.objects.get(user_id = u_id)
        e_id = Event.objects.all()
        context = {
            "u_id" : u_id,
            "c_id" : c_id,
            "e_id" : e_id
        }
        return render (request, "myapps/all_event.html", context)
    else:
        return render(request, "myapps/all_event.html", context)
    
def mem_all_notice(request):
    if "email" in request.session:
        u_id = User.objects.get(email = request.session["email"])
        m_id = Add_member.objects.get(m_user_id = u_id)
        n_id = Add_notice.objects.all()
        context = {
            "u_id" :u_id,
            "n_id" : n_id,
            "m_id" : m_id
        }
        return render (request, "myapps/mem_all_notice.html", context)
    else:
        return render (request, "myapps/login.html")
        
def mem_all_member(request):
    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        m_id = Add_member.objects.get(m_user_id=u_id)
        m1_id = Add_member.objects.all()
        context = {
            "m1_id" : m1_id,
            "u_id" : u_id,
            "m_id" : m_id
        }
        return render(request, "myapps/mem_all_members.html", context)
    else:
        return render(request, "myapps/login.html")

def mem_all_event(request):

    if "email" in request.session :
        u_id = User.objects.get(email = request.session["email"])
        m_id = Add_member.objects.get(m_user_id=u_id)
        e_id = Event.objects.all()
        context = {
            "m_id" : m_id,
            "u_id" : u_id,
            "e_id" : e_id
        }
        return render(request, "myapps/mem_all_event.html", context)
    else:
        return render(request, "myapps/login.html")

