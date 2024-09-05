from django.db import models
from django.utils import timezone

from branches.models import Branches
from accounts.models import Church
from members.models import Member

class AttendanceProgram(models.Model):
	church = models.ForeignKey(Church, related_name='attendanceprogram_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='attendanceprogram_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	programid = models.IntegerField(blank=True, null=True, default=0 )
	date = models.DateField(null=True, blank=True, default=timezone.now)
	attendancetype = models.CharField(max_length=255, blank=True, null=True, default='Church Attendance' )
	male = models.BigIntegerField(blank=True, null=True, default=0 )
	female = models.BigIntegerField(blank=True, null=True, default=0 )
	children = models.BigIntegerField(blank=True, null=True, default=0 )
	total = models.BigIntegerField(blank=True, null=True, default=0 )
	status = models.BooleanField(blank=True,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return self.attendancetype

class Attendance(models.Model):
	church = models.ForeignKey(Church, related_name='attendance_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='attendance_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	attendancetype = models.CharField(max_length=255, blank=True, null=True, default='Church Attendance' )
	attendantid = models.CharField(max_length=100, blank=True, null=True)
	programid = models.BigIntegerField(blank=True, null=True, default=0 )
	membername = models.ForeignKey(Member, related_name='attendance_member', default='', blank=True, null=True, on_delete=models.SET_NULL)
	attendance = models.BooleanField(blank=True,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return self.attendancetype