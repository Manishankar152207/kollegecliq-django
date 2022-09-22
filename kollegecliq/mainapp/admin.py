from django.contrib import admin
from mainapp.models import RegisteredUsers
# Register your models here.
@admin.register(RegisteredUsers)
class InfoRegisteredUsers(admin.ModelAdmin):
    list_display = ['user_id','username','email','phone','password','created_on','updated_on','is_live']
