from django.contrib import admin

from techpanel.models import AdvancedUser, Sales, SalesUserAccount, TechChat

@admin.register(AdvancedUser)
class AdvancedUserAdmin(admin.ModelAdmin):
	search_fields = ('userid', 'firstname', 'middlename', 'lastname', 'telephone', 'email')
	list_display = ('userid', 'firstname', 'middlename', 'lastname', 'telephone', 'email')

@admin.register(TechChat)
class TechChatAdmin(admin.ModelAdmin):
	search_fields = ('message', 'datecreated')
	list_display = ('chatuser', 'role', 'message', 'datecreated')

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
	search_fields = ('premiumamount', 'packagetype', 'commissionrate', 'commissionamount')
	list_display = ('church', 'branch', 'premiumamount', 'packagetype', 'commissionrate', 'commissionamount')

@admin.register(SalesUserAccount)
class SalesUserAccountAdmin(admin.ModelAdmin):
	search_fields = ('user', 'amount')
	list_display = ('user', 'amount')



