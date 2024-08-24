from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from branches.utils import generate_slug
from datetime import datetime, timedelta
from churchprofile.models import ChurchProfile



# Create your models here.
class Branches(models.Model):
	# paymentplan choices
	PAYMENT_PLAN_CHOICES = (('Basic','Basic'),('Gold','Gold'), ('Diamond','Diamond'))
	
	church = models.ForeignKey(ChurchProfile, related_name='branches_church', default='', blank=True, null=True, on_delete=models.SET_NULL)
	subhead = models.CharField(max_length=50, blank=True, null=True)
	branchname = models.CharField(max_length=255, blank=True, null=True )
	subheadalias = models.CharField(max_length=255, blank=True, null=True )
	branchphotograph = models.ImageField(upload_to = 'branchphotos', blank=True, null=True )	
	slug = models.SlugField(unique=True, null=True, blank=True, max_length=255)
	location = models.CharField(max_length=255, blank=True, null=True )
	country = models.CharField(max_length=255, blank=True, null=True )
	residentialaddress = models.TextField(blank=True, null=True )
	postaladdress = models.TextField(blank=True, null=True )
	telephone = models.CharField(max_length=255, blank=True, null=True )
	fax = models.CharField(max_length=255, blank=True, null=True )
	email = models.EmailField(max_length=255, blank=True, null=True )
	website = models.URLField(max_length=255, blank=True, null=True )
	headfullname = models.CharField(max_length=255, blank=True, null=True )
	headtelephone = models.CharField(max_length=255, blank=True, null=True )
	heademail = models.EmailField(max_length=255, blank=True, null=True )
	headposition = models.CharField(max_length=255, blank=True, null=True )
	paymentplan = models.CharField(max_length=255, blank=False, null=True,  choices = PAYMENT_PLAN_CHOICES, default = 'Basic')
	chargeamount = models.DecimalField(max_digits=255, decimal_places=2, default=0)	
	nextchargedate = models.DateField(default= datetime.now() + timedelta(1*365/12), blank = True, null=True )
	keycode = models.CharField(max_length=255, blank=True, null=True )
	connectedtoserver = models.BooleanField(blank=True,  default=False)
	module_dashboard = models.BooleanField(blank=False,  default=True)
	module_members = models.BooleanField(blank=False,  default=True)
	module_members_add = models.BooleanField(blank=False,  default=True)
	module_members_update = models.BooleanField(blank=False,  default=True)
	module_members_delete = models.BooleanField(blank=False,  default=True)
	module_guests = models.BooleanField(blank=False,  default=True)
	module_guests_add = models.BooleanField(blank=False,  default=True)
	module_guests_update = models.BooleanField(blank=False,  default=True)
	module_guests_delete = models.BooleanField(blank=False,  default=True)
	module_attendance = models.BooleanField(blank=False,  default=True)
	module_notifier = models.BooleanField(blank=False,  default=True)
	module_notifier_sms = models.BooleanField(blank=False,  default=True)
	module_notifier_emails = models.BooleanField(blank=False,  default=True)
	module_notifier_mobileapp = models.BooleanField(blank=False,  default=True)
	module_notifier_settings = models.BooleanField(blank=False,  default=True)
	module_finance = models.BooleanField(blank=False,  default=True)
	module_finance_individualincome = models.BooleanField(blank=False,  default=True)
	module_finance_bulkincome = models.BooleanField(blank=False,  default=True)
	module_finance_expenditure = models.BooleanField(blank=False,  default=True)
	module_finance_accountsetup = models.BooleanField(blank=False,  default=True)
	module_reports = models.BooleanField(blank=False,  default=True)
	module_reports_branch = models.BooleanField(blank=False,  default=True)
	module_reports_subbranch = models.BooleanField(blank=False,  default=True)
	module_administration = models.BooleanField(blank=False,  default=True)
	module_administration_branchprofile = models.BooleanField(blank=False,  default=True)
	module_administration_branchusers = models.BooleanField(blank=False,  default=True)
	module_administration_choices = models.BooleanField(blank=False,  default=True)
	headquarters = models.BooleanField(blank=False,  default=False)
	confirmed = models.BooleanField(blank=True,  default=False)
	deleted = models.BooleanField(blank=False,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		try:
			if not self.is_update_view:
				self.slug = generate_slug(self, self.branchname)
		except:
			self.slug = generate_slug(self, self.branchname)

		super(Branches, self).save(*args, **kwargs)


	def __str__(self):  
		return self.slug

class BranchUser(models.Model):
	church = models.ForeignKey(ChurchProfile, related_name="chuserprofile", default='', blank=True, null=True, on_delete=models.SET_NULL)
	branch = models.ForeignKey(Branches, related_name="chuserbranch", default='' , on_delete=models.PROTECT)
	user = models.OneToOneField(User, related_name="branchprofile", default='', blank=True, null=True, on_delete=models.SET_NULL)
	memberid = models.CharField(max_length=100, null=True, blank=True) 
	email = models.EmailField(max_length=255, blank=True, null=True )
	userposition = models.CharField(max_length=255, blank=True, null=True )
	membername = models.CharField(max_length=255, blank=True, null=True )
	username = models.CharField(max_length=255, blank=True, null=True )
	password = models.CharField(max_length=255, blank=True, null=True )
	securityquestion = models.CharField(max_length=255, blank=True, null=True )
	securityanswer = models.CharField(max_length=255, blank=True, null=True )
	module_dashboard = models.BooleanField(blank=False,  default=True)
	module_members = models.BooleanField(blank=False,  default=True)
	module_members_add = models.BooleanField(blank=False,  default=True)
	module_members_update = models.BooleanField(blank=False,  default=True)
	module_members_delete = models.BooleanField(blank=False,  default=True)
	module_guests = models.BooleanField(blank=False,  default=True)
	module_guests_add = models.BooleanField(blank=False,  default=True)
	module_guests_update = models.BooleanField(blank=False,  default=True)
	module_guests_delete = models.BooleanField(blank=False,  default=True)
	module_attendance = models.BooleanField(blank=False,  default=True)
	module_notifier = models.BooleanField(blank=False,  default=True)
	module_notifier_sms = models.BooleanField(blank=False,  default=True)
	module_notifier_emails = models.BooleanField(blank=False,  default=True)
	module_notifier_mobileapp = models.BooleanField(blank=False,  default=True)
	module_notifier_settings = models.BooleanField(blank=False,  default=True)
	module_finance = models.BooleanField(blank=False,  default=True)
	module_finance_individualincome = models.BooleanField(blank=False,  default=True)
	module_finance_bulkincome = models.BooleanField(blank=False,  default=True)
	module_finance_expenditure = models.BooleanField(blank=True,  default=True)
	module_finance_accountsetup = models.BooleanField(blank=False,  default=True)
	module_reports = models.BooleanField(blank=False,  default=True)
	module_reports_branch = models.BooleanField(blank=False,  default=True)
	module_reports_subbranch = models.BooleanField(blank=False,  default=True)
	module_administration = models.BooleanField(blank=False,  default=True)
	module_administration_branchprofile = models.BooleanField(blank=False,  default=True)
	module_administration_branchusers = models.BooleanField(blank=False,  default=True)
	module_administration_choices = models.BooleanField(blank=False,  default=True)
	firsttimeuse = models.BooleanField(blank=True,  default=False)
	deleted = models.BooleanField(blank=False,  default=False)
	deactivated = models.BooleanField(blank=True,  default=False)
	datecreated = models.DateTimeField(default=timezone.now)


	def __str__(self):  
		return self.membername