from django.contrib import admin

from reports.models import BranchReport

@admin.register(BranchReport)
class BranchReportAdmin(admin.ModelAdmin):
	search_fields = ('title', 'datecreated')
	list_display = ('title', 'datecreated', 'branch', 'church')