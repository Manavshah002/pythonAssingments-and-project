from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Chairman)
admin.site.register(Add_member)
admin.site.register(Add_notice)
admin.site.register(Event)

