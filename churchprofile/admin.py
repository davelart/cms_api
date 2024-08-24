from django.contrib import admin

from churchprofile.models import *

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
	search_fields = ('churchname', 'registererfullname', 'registerertelephonecode', 'registerertelephone', 'registereremail', 'country', 'code', 'confirmed')
	list_display = ('churchname', 'registererfullname', 'registerertelephonecode', 'registerertelephone', 'registereremail', 'country', 'code', 'confirmed')

@admin.register(ChurchProfile)
class ChurchProfileAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("churchname",)}
	search_fields = ('churchname', 'telephone', 'email', 'website', 'registererfullname', 'country', 'code', 'datecreated')
	list_display = ('churchname', 'telephone', 'email', 'website', 'registererfullname', 'country', 'code', 'datecreated')