from django.contrib import admin
from Accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    
