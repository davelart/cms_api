from django.contrib import admin
from .models import AttendanceProgram, Attendance

@admin.register(AttendanceProgram)
class AttendanceProgramAdmin(admin.ModelAdmin):
	search_fields = ('datecreated', 'attendancetype', 'male', 'female', 'total')
	list_display = ('attendancetype', 'male', 'female', 'total', 'status', 'datecreated', 'branch', 'church')  

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('membername', 'programid', 'branch', 'church', 'attendance')