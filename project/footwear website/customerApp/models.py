from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length= 500)
    message = models.TextField()
    
    
    def __str__(self):
        return self.fname + " | " + self.email
    
    
class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(unique=True)
    address = models.TextField()
    password = models.CharField(max_length=50)
    
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
    
    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email)
    
    def __str__(self) -> str:
        return self.fname + " " + self.email

class Authenticate(models.Model):
    email = models.EmailField()
    auth_token = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
        
