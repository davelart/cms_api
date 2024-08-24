from django.db import models
from django.utils import timezone

from branches.models import Branches
from churchprofile.models import ChurchProfile

class BranchReport(models.Model):
	church = models.ForeignKey(ChurchProfile, related_name='branchreport_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='branchreport_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=255)
	fulltext = models.TextField(blank=True, null=True )	
	datecreated = models.DateTimeField(default=timezone.now)



	def __str__(self):  
		return self.title
