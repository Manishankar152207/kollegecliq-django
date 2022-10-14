from django.contrib import admin
from mainapp.models import RegisteredUsers,Contact,RegisteredCollege
# Register your models here.
@admin.register(RegisteredUsers)
class InfoRegisteredUsers(admin.ModelAdmin):
    list_display = ['user_id','username','name','email','phone','created_on','updated_on','is_live']

@admin.register(RegisteredCollege)
class InfoRegisteredCollege(admin.ModelAdmin):
    list_display = ['user_id','name','email','phone','created_on','updated_on','is_live']

@admin.register(Contact)
class InfoContact(admin.ModelAdmin):
    list_display = ['name','email','message','date']
