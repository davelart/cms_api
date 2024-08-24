from django.contrib import admin

from administration.models import Choices, ChurchGroup

@admin.register(ChurchGroup)
class ChurchGroupAdmin(admin.ModelAdmin):
	search_fields = ('churchgroup', 'datecreated')
	list_display = ('churchgroup', 'branch', 'church')
    
@admin.register(Choices)
class ChoicesAdmin(admin.ModelAdmin):
	search_fields = ('choicetype', 'choice', 'church__churchname' 'branch__branchname')
	list_display = ('choicetype', 'choice', 'church', 'branch')