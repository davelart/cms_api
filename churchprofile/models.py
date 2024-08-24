from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from churchprofile.utils import generate_slug

class Register(models.Model):
	churchname = models.CharField(max_length=255, blank=True, null=True)
	registererfullname = models.CharField(max_length=255, blank=True, null=True)
	registereremail = models.EmailField(max_length=255, blank=True, null=True)
	registerertelephonecode = models.CharField(max_length=255, null=True,  blank=True)
	registerertelephone = models.CharField(max_length=255, blank=True, null=True)
	paymentplan = models.CharField(max_length=255, blank=True, null=True)	
	country = models.CharField(max_length=100, blank=True, null=True )
	code = models.CharField(max_length=100, blank=True, null=True, default='')
	confirmed = models.BooleanField(blank=False,  default=False)
	expired_date = models.BigIntegerField(default=0, blank=True, null=True)
	datecreated = models.DateTimeField(default=timezone.now)

class ChurchProfile(models.Model):
	age = 0
	user = models.ForeignKey(User, related_name="churchprofile", on_delete=models.PROTECT)
	country = models.CharField(max_length=100, blank=True, null=True )
	churchname = models.CharField(max_length=255, null=True,  blank=True)
	slug = models.SlugField(unique=True, null=True, blank=True, max_length=255)
	residentialaddress = models.TextField(null=True,  blank=True)
	postaladdress = models.TextField(null=True,  blank=True)
	telephone = models.CharField(max_length=255, null=True,  blank=True)
	email = models.EmailField(max_length=255, blank=True, null=True)
	website = models.URLField(max_length=255, null=True,  blank=True)
	logo = models.ImageField(upload_to = 'churchlogos', blank=True, null=True )
	motto = models.TextField(max_length=255, null=True,  blank=True)
	colours = models.CharField(max_length=100, blank=True, null=True )
	registererfullname = models.CharField(max_length=255, null=True,  blank=True)
	registereremail = models.EmailField(max_length=255, null=True,  blank=True)
	registerertelephonecode = models.CharField(max_length=255, null=True,  blank=True)	
	registerertelephone = models.CharField(max_length=255, null=True,  blank=True)	
	registererusername = models.CharField(max_length=255, null=True,  blank=True)	
	registererpassword = models.CharField(max_length=255, null=True,  blank=True)
	securityquestion = models.CharField(max_length=255, null=True,  blank=True)	
	securityanswer = models.CharField(max_length=255, null=True,  blank=True)
	totalnotifierpoints = models.IntegerField(null=True,  blank=True, default=0)
	assignednotifierpoints = models.IntegerField(null=True,  blank=True, default=0)
	freenotifierpoints = models.IntegerField(null=True,  blank=True, default=0)
	module_dashboard = models.BooleanField(blank=False,  default=True)
	module_branches = models.BooleanField(blank=False,  default=True)
	module_branchusers = models.BooleanField(blank=False,  default=True)
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
	module_finance_trialbalance = models.BooleanField(blank=False,  default=True)
	module_finance_balancesheet = models.BooleanField(blank=False,  default=True)
	module_finance_finalaccounts = models.BooleanField(blank=False,  default=True)
	module_finance_accountsetup = models.BooleanField(blank=False,  default=True)
	module_branchreport = models.BooleanField(blank=False,  default=True)
	module_grandreport = models.BooleanField(blank=False,  default=True)
	module_support = models.BooleanField(blank=False,  default=True)
	module_administration = models.BooleanField(blank=False,  default=True)
	module_administration_payment = models.BooleanField(blank=False,  default=True)
	module_administration_profile = models.BooleanField(blank=False,  default=True)
	module_administration_branchprofile = models.BooleanField(blank=False,  default=True)
	module_administration_branchusers = models.BooleanField(blank=False,  default=True)
	module_administration_choices = models.BooleanField(blank=False,  default=True)
	
	code = models.CharField(max_length=200, null=True, blank=True)
	datecreated = models.DateTimeField(default=timezone.now)
	deactivated = models.BooleanField(blank=True,  default=False)

	def save(self, *args, **kwargs):
		try:
			if not self.is_update_view:
				self.slug = generate_slug(self, self.churchname)
		except:
			self.slug = generate_slug(self, self.churchname)

		super(ChurchProfile, self).save(*args, **kwargs)
		

	def __str__(self):  
		return self.slug