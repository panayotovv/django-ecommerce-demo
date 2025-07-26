from django.contrib import admin
from Programs.models import Programs


@admin.register(Programs)
class ProgramsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

