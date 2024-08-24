from django.contrib import admin
from .models import Guests

@admin.register(Guests)
class GuestsAdmin(admin.ModelAdmin):
	search_fields = ('firstname', 'middlename', 'lastname')
	list_display = ('firstname', 'middlename', 'lastname', 'branch', 'church')