from django.contrib import admin
from .models import Account, Church

@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    search_fields = ('name', 'logo', 'phone', 'email', 'fullname', 'phone', 'email', 'address', 'payment_plan', 'next_expiry_date')
    list_display = ('name', 'logo', 'phone', 'email', 'fullname', 'phone', 'email', 'address', 'payment_plan', 'next_expiry_date')
    list_filter = ['active', ]
    readonly_fields = ['identifier',]

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'church__name', 'identifier', 'confirmed')
    list_display = ['identifier', 'user', 'church', 'confirmed']