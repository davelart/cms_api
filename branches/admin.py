from django.contrib import admin
from branches.models import *

@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('branchname',)}
    search_fields = ('branchname', 'location', 'residentialaddress', 'keycode')
    list_display = ('branchname', 'location', 'church', 'keycode', 'confirmed')

@admin.register(BranchUser)
class BranchUserAdmin(admin.ModelAdmin):
    search_fields = ('branch', 'membername', 'username')
    list_display = ('branch', 'membername', 'username', 'church')