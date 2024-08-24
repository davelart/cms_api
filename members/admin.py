from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    search_fields = ('firstname', 'middlename', 'lastname')
    list_display = ('firstname', 'middlename', 'lastname', 'phonenumber1', 'emailaddress1')