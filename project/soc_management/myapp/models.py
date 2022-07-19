from django.db import models
from django.utils import timezone
import math

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique = True, max_length = 50)
    password = models.CharField(max_length = 30)
    otp = models.IntegerField(default= 459)
    role = models.CharField(max_length= 10)
    is_active = models.BooleanField(default=False)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Chairman(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)
    block_no = models.CharField(max_length = 50, null = True)
    house_no = models.CharField(max_length = 50, null = True)
    about_me = models.TextField(max_length = 5000, null = True)
    pic = models.FileField(default = "media/images/default.png")
    
    def __str__(self):
        return self.firstname
    
gender = (("Male","male"), ("Female", "female"), ("Other", "other"))

class Add_member(models.Model):
    m_user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    m_f_name = models.CharField(max_length=50)
    m_l_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=10)
    gender = models.CharField(max_length=15, choices=gender)
    work = models.CharField(max_length=50, null=True)
    m_block_no = models.CharField(max_length=50, null=True)
    m_house_no = models.CharField(max_length=50, null=True)
    family_member = models.IntegerField(null=True)
    vehicle = models.IntegerField(null = True)
    contact_no = models.IntegerField(null = True)
    m_about_me = models.TextField(max_length = 5000, null = True)
    m_pic = models.FileField(default="media/images/member/m_default.png")
    
    def __str__(self):
        return self.m_f_name
 
       
class Add_notice(models.Model):
    user_id = models.ForeignKey(Chairman, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    n_pic = models.FileField(upload_to="media/images/notice", null=True)
    n_video = models.FileField(upload_to="media/video", null=True)
    content = models.TextField(null=True, max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    def whenpublished(self):
        now = timezone.now()
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"
            
class Event(models.Model):
    user_id = models.ForeignKey(Chairman, on_delete = models.CASCADE)
    e_title = models.CharField(max_length=50)
    e_pic = models.FileField(upload_to="media/images/notice", null=True)
    e_venue = models.CharField(max_length = 2000)
    e_date = models.DateField(max_length = 10)
    e_content = models.TextField(null=True, max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.e_title
    
    
    def e_whenpublished(self):
        now = timezone.now()
        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"