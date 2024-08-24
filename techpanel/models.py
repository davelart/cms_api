from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

from branches.models import Branches
from churchprofile.models import ChurchProfile

class AdvancedUser(models.Model):
	photograph = models.ImageField(upload_to = 'advancedusersphotos', blank=True, null=True)
	user = models.ForeignKey(User, related_name="advuserprofile", on_delete=models.PROTECT)
	userid = models.CharField(max_length=255, blank=True, null=True )
	firstname = models.CharField(max_length=255, blank=True, null=True )
	middlename = models.CharField(max_length=255, blank=True, null=True )
	lastname = models.CharField(max_length=255, blank=True, null=True )
	gender = models.CharField(max_length=255, blank=True, null=True)
	dateofbirth = models.DateField(blank = True, null=True )
	telephone = models.CharField(max_length=255, blank=True, null=True )
	email = models.EmailField(max_length=255, blank=True, null=True )
	country = models.CharField(max_length=255, blank=True, null=True )
	levelofeducation = models.CharField(max_length=255, blank=True, null=True )
	salesskills = models.CharField(max_length=255, blank=True, null=True )
	summary = models.CharField(max_length=255, blank=True, null=True )
	curriculumvitae = models.FileField(upload_to='advanceduserscv', max_length=255, blank=True, null=True )
	username = models.CharField(max_length=255, blank=True, null=True )
	password = models.CharField(max_length=255, blank=True, null=True )
	role = models.CharField(max_length=255, blank=True, null=True )	
	module_profile = models.BooleanField(blank=False,  default=True)
	module_sales = models.BooleanField(blank=False,  default=False)
	module_documentation = models.BooleanField(blank=False,  default=True)
	module_admin = models.BooleanField(blank=False,  default=False)
	module_church = models.BooleanField(blank=False,  default=False)
	module_chat = models.BooleanField(blank=False,  default=False)
	module_system = models.BooleanField(blank=False,  default=False)
	confirmed = models.BooleanField(blank=True,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		# return self.userid
		return 'user'


class SalesUserAccount(models.Model):
	user = models.ForeignKey(User, related_name='salesusracc', blank=True, null=True, on_delete=models.PROTECT )
	userid = models.CharField(max_length=255, blank=True, null=True )
	amount = models.CharField(max_length=255, blank=True, null=True )
	activestatus = models.BooleanField(blank=True,  default=True)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return 'self.userid'


class Sales(models.Model):
	church = models.ForeignKey(ChurchProfile, related_name='sales_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='sales_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)
	premiumamount = models.DecimalField(max_digits=100, decimal_places=1, blank=True, null=True )
	packagetype = models.CharField(max_length=255, blank=True, null=True )
	commissionrate = models.CharField(max_length=255, blank=True, null=True )
	commissionamount = models.DecimalField(max_digits=100, decimal_places=1, blank=True, null=True )
	commissionagentid = models.CharField(max_length=255, blank=True, null=True )
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return self.commissionagentid

class TechChatTicket(models.Model):
	church = models.ForeignKey(ChurchProfile, related_name='techchatticket_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name='chatticket_branch', default='', blank=True, null=True, on_delete=models.SET_NULL)	
	chatuser = models.ForeignKey(User, related_name='chatticketuser', default='', blank=True, null=True, on_delete=models.SET_NULL)
	chatadmin = models.ForeignKey(User, related_name="chatticketadmin", default='', blank=True, null=True, on_delete=models.SET_NULL)
	role = models.CharField(max_length=255, blank=True, null=True)
	message = models.CharField(max_length=255, blank=True, null=True)
	target = models.CharField(max_length=255, blank=True, null=True)
	sent = models.BooleanField(blank=True,  default=False)
	received = models.BooleanField(blank=True,  default=False)
	read = models.BooleanField(blank=True,  default=False)	
	resolved = models.BooleanField(blank=True,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return self.message

class TechChat(models.Model):
	# church = models.ForeignKey(ChurchProfile, related_name='techchat_church', default='')
	# branch = models.ForeignKey(Branches, related_name='techchat_branch', default='')	
	chatuser = models.ForeignKey(User, related_name='chatuser', default='', blank=True, null=True, on_delete=models.SET_NULL)
	role = models.CharField(max_length=255, blank=True, null=True)
	message = models.CharField(max_length=255, blank=True, null=True)
	target = models.CharField(max_length=255, blank=True, null=True)
	sent = models.BooleanField(blank=True,  default=False)
	received = models.BooleanField(blank=True,  default=False)
	read = models.BooleanField(blank=True,  default=False)	
	resolved = models.BooleanField(blank=True,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)

	def __str__(self):  
		return self.message