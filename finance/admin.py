from django.contrib import admin
from .models import AccountSetup, AccountPayment, AccountExpenditure

@admin.register(AccountSetup)
class AccountSetupAdmin(admin.ModelAdmin):
	search_fields = ('accountname', 'accounttype', 'purpose', 'datecreated')
	list_display = ('accountname', 'accounttype', 'purpose', 'datecreated', 'church', 'branch')

@admin.register(AccountPayment)
class AccountPaymentAdmin(admin.ModelAdmin):
	search_fields = ('accountname', 'payerfullname', 'amount', 'datecreated')
	list_display = ('accountname', 'payerfullname', 'amount', 'datecreated', 'church', 'branch')
	
@admin.register(AccountExpenditure)
class AccountExpenditureAdmin(admin.ModelAdmin):
	search_fields = ('title', 'description', 'amount', 'approvedby', 'datecreated')
	list_display = ('title', 'description', 'amount', 'approvedby', 'datecreated', 'church', 'branch')