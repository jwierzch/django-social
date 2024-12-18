from django.contrib import admin
from django.contrib.auth.models import  User, Group
from .models import Dweet, Profile, gimage

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Dweet)
admin.site.register(gimage)